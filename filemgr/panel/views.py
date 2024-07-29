import pathlib

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Plant
from .forms import UploadFileForm



""" 
The __file__ variable is a special variable in Python that contains the path to the script that is currently being executed.  
pathlib.Path(__file__) creates a Path object for the current script's path.
The resolve() method returns the absolute path of the Path object, resolving any symbolic links and relative path components. Essentially, it converts the path to its absolute form.
"""
this_dir = pathlib.Path(__file__).resolve().parent
#print('This views module is in directory: ', this_dir)

index_template = this_dir / 'templates/panel/index.html'
print('This template html is in directory: ', index_template)




# Create your views here.
def index_view(request):
    context = {
        "button_name": "Upload File",
        "file_name": "The name of the file uploaded"
    }
    return render(request, index_template, context)


def index_view_static(request):
    return HttpResponse("This is an index page.")


def hello_world_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello, world!</h1>")
    #return "Hello world!"


# not tested yet
def upload_image_view(request, *args, **kwargs):
    if request.method == 'POST':
        plant = Plant(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])  # todo: replace 'file' with other names?
            return HttpResponseRedirect('/success/url')  # todo: sucess url need to be replaced?
        else:
            print('Form uploaded is not valid!')
    else:
        form = UploadFileForm()

    context = {
        "button_name": "Upload File",        
        "file_name": "The name of the file uploaded",
        "form": form,  # todo: form need to be assigned to after Upload File button is clicked
    }
    return render(request, index_template, context)

def upload_excel_view(request, *args, **kwargs):
    pass 

def upload_pdf_view(request, *args, **kwargs):
    pass

def upload_txt_view(request, *args, **kwargs):
    pass

# not tested yet
def upload_file_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])  # todo: replace 'file' with other names?
            return HttpResponseRedirect('/success/url')  # todo: sucess url need to be replaced?
        else:
            print('Form uploaded is not valid!')
    else:
        form = UploadFileForm()

    context = {
        "button_name": "Upload File",        
        "file_name": "The name of the file uploaded",
        "form": form,  # todo: form need to be assigned to after Upload File button is clicked
    }
    return render(request, index_template, context)
    
# todo: this function is incomplete and only serves demonstration purpose for now
def handle_uploaded_file(f):
    """ 
    Looping over UploadedFile.chunks() instead of using read() ensures that large files don’t overwhelm your system’s memory.
    """
    with open("some/file/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


