import pathlib

from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit


""" 
The __file__ variable is a special variable in Python that contains the path to the script that is currently being executed.  
pathlib.Path(__file__) creates a Path object for the current script's path.
The resolve() method returns the absolute path of the Path object, resolving any symbolic links and relative path components. Essentially, it converts the path to its absolute form.
"""
this_dir = pathlib.Path(__file__).resolve().parent
#print(f"this directory is: {this_dir}")


# Global variables
company_name = 'Bull Company'
head1 = 'This is a rendered h1 variable'


# Create your views here.


def home_view_rendered(request, *args, **kwargs):   
    page_name = 'Home'
    page_visits = PageVisit.objects.filter(path=request.path)
    total_visits = PageVisit.objects.all()

    template_name = 'home.html'
    
    context = {
        "company_name": company_name,
        "page_name": page_name,
        "head1": head1,
        "page_visits": page_visits.count(),
        "total_visits": total_visits.count(),
    }

    PageVisit.objects.create(path=request.path)

    return render(request, template_name, context)

def home_view_dynamic(request, *args, **kwargs):
    head1 = "This is a dynamic h1"
    context = {
        "head1": head1,
    }
    home_html_ = """ <html>
    <h1>{head1}</h1>
    </html> """.format(**context)
    return HttpResponse(home_html_)

def home_view_static(request, *args, **kwargs):
    return HttpResponse("This is a home page.")  