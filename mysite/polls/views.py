from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.db.models import F
from django.utils import timezone

from .models import Question, Choice

# Create your views here.


# -------------------------------------------------------------------------- #
# --------------- Use Generic Views: Less Code is Better ------------------- #
# -------------------------------------------------------------------------- #

# https://docs.djangoproject.com/en/5.0/topics/class-based-views/

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the lastest ten published questions."""
        # __lte is less than or equal to
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
        

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"





# -------------------------------------------------------------------------- #
# --------------------------- Use Defined Views ---------------------------- #
# -------------------------------------------------------------------------- #

# request and response documentation
# https://docs.djangoproject.com/en/5.0/ref/request-response/

def index(request: HttpRequest):
    """
    request: this is a HttpRequest object

    The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def index_no_render(request: HttpRequest):
    """This function loads the template called polls/index.html and passes it a context. The context is a dictionary mapping template variable names to Python objects.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }    
    return HttpResponse(template.render(context, request))




def detail(request: HttpRequest, question_id):
    """The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the models manager. It raises Http404 if the object doesnt exist.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def detail_no_shortcut(request: HttpRequest, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {"question": question})

def detail_static(request: HttpRequest, question_id):
    return HttpResponse("You're looking at question %s." % question_id)








def vote(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context = {
            "question": question,
            "error_message": "You didn't select a choice.",
        }
        return render(request, 'polls/detail.html', context)
    else:
        # instructs the database to increase the vote count by 1.
        # https://docs.djangoproject.com/en/5.0/ref/models/expressions/#avoiding-race-conditions-using-f
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # HttpResponseRedirect takes a single argument: the URL to which the user will be redirected (see the following point for how we construct the URL in this case).
        # Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
        # The reverse() function helps avoid having to hardcode a URL in the view function. It is given the name of the view, in this case "polls:results", that we want to pass control to and the variable portion of the URL pattern that points to that view. In this case, using the URLconf we set up in Tutorial 3, this reverse() call will return a string "/polls/3/results/", where the 3 is the value of question.id. This redirected URL will then call the 'results' view to display the final page.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def vote_static(request: HttpRequest, question_id):
    return HttpResponse("You're voting on question %s." % question_id)





def results(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {"question": question})


def results_static(request: HttpRequest, question_id):
    response = "You're looking at the results of question %s. "
    return HttpResponse(response % question_id)