import pathlib

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import ModelWithImageField, ModelWithFileField
from .forms import ModelFormWithImageField, ModelFormWithFileField, UploadFileForm


""" 
The __file__ variable is a special variable in Python that contains the path to the script that is currently being executed.  
pathlib.Path(__file__) creates a Path object for the current script's path.
The resolve() method returns the absolute path of the Path object, resolving any symbolic links and relative path components. Essentially, it converts the path to its absolute form.
"""
this_dir = pathlib.Path(__file__).resolve().parent
#print('This views module is in directory: ', this_dir)

index_template = this_dir / 'templates/panel/index.html'
#print('This template html is in directory: ', index_template)

upload_template = this_dir / 'templates/panel/upload.html'

# Create your views here.
def load_index(request):
    context = {
        "button_name": "Upload File",
        "file_name": "The name of the file uploaded",
    }
    return render(request, index_template, context)

def load_static_index(request):
    return HttpResponse("This is an index page.")



def upload_image(request, *args, **kwargs):
    context = {
        "form": ModelFormWithImageField(),
    }
    return render(request, upload_template, context)


# not tested yet
def upload_file(request, *args, **kwargs):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url')  # todo: sucess url need to be replaced?
        else:
            print('Form uploaded is not valid!')
    else:
        form = ModelFormWithFileField()

    context = {
        "form": form,  # todo: form need to be assigned to after Upload File button is clicked
    }
    return render(request, upload_template, context)




