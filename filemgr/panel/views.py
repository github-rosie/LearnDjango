import pathlib

from django.shortcuts import render
from django.http import HttpResponse



""" 
The __file__ variable is a special variable in Python that contains the path to the script that is currently being executed.  
pathlib.Path(__file__) creates a Path object for the current script's path.
The resolve() method returns the absolute path of the Path object, resolving any symbolic links and relative path components. Essentially, it converts the path to its absolute form.
"""
this_dir = pathlib.Path(__file__).resolve().parent



# Create your views here.
def index_view_static(request):
    return HttpResponse("This is the index page.")

def hello_world_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello, world!</h1>")
    #return "Hello world!"