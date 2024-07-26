import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question
from .views import IndexView



"""
# https://docs.djangoproject.com/en/5.0/intro/tutorial05/

As long as your tests are sensibly arranged, they wont become unmanageable. Good rules-of-thumb include having:
- a separate TestClass for each model or view
- a separate test method for each set of conditions you want to test
- test method names that describe their function

# Run tests in Terminal: ...\> py manage.py test polls
"""



# URL patterns as defined in polls.urls.py file 
index_url_pattern = "polls:index"
detail_url_pattern = "polls:detail"
vote_url_pattern = "polls:vote"
results_url_pattern = "polls:results"

index_view_context_obj_name = "latest_question_list"




class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """was_published_recently() returns False for questions whose pub_date is in the future."""
        future_time = timezone.now() + datetime.timedelta(seconds=1)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """was_published_recently() returns False for questions whose pub_date is older than 1 day."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """was_published_recently() returns True for questions whose pub_date is within the last day."""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)




def create_question(question_text: str, days=0, hours=0, minutes=0, seconds=0):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """ If no questions exist, an appropriate message is displayed. """
        # reverse("polls:index"): This function is used to resolve the URL for the named URL pattern "polls:index". The reverse function takes the name of a URL pattern (as defined in polls app's urls.py file) and returns the corresponding URL as a string.
        # self.client is an instance of django.test.Client, a class provided by Django for simulating client requests in test cases.
        # The get method on this client instance is used to simulate a GET request to the URL obtained from the reverse function.
        # Essentially, this line sends an HTTP GET request to the URL for the polls:index view.
        # Putting it all together, this line is simulating a client making a GET request to the polls:index view and storing the resulting HTTP response in the response variable.
        response = self.client.get(reverse(index_url_pattern))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context[index_view_context_obj_name], [])

    def test_past_question(self):
        """ Questions with a pub_date in the past are displayed on the index page. """
        question = create_question("Past question.", seconds=-1)
        response = self.client.get(reverse(index_url_pattern))
        self.assertQuerysetEqual(response.context[index_view_context_obj_name], [question])

    def test_future_question(self):
        """ Questions with a pub_date in the future aren't displayed on the index page.
        """
        create_question(question_text="Future question.", seconds=1)
        response = self.client.get(reverse(index_url_pattern))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context[index_view_context_obj_name], [])

    def test_future_question_and_past_answer(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", seconds=-1)
        future_question = create_question(question_text="Future question.", seconds=1)
        response = self.client.get(reverse(index_url_pattern))
        self.assertQuerySetEqual(
            response.context[index_view_context_obj_name],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", seconds=-1)
        question2 = create_question(question_text="Past question 2.", seconds=0)
        response = self.client.get(reverse(index_url_pattern))
        self.assertQuerySetEqual(
            response.context[index_view_context_obj_name],
            [question2, question1],
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", seconds=1)
        url = reverse(detail_url_pattern, args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", seconds=-1)
        url = reverse(detail_url_pattern, args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)