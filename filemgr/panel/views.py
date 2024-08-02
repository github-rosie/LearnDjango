import pathlib

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import ModelWithImageField, ModelWithFileField
from .forms import ModelFormWithImageField, ModelFormWithFileField


# https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/

""" 
The __file__ variable is a special variable in Python that contains the path to the script that is currently being executed.  
pathlib.Path(__file__) creates a Path object for the current script's path.
The resolve() method returns the absolute path of the Path object, resolving any symbolic links and relative path components. Essentially, it converts the path to its absolute form.
"""
this_dir = pathlib.Path(__file__).resolve().parent
#print('This views module is in directory: ', this_dir)


# Set the directories of templates
index_template = this_dir / 'templates/panel/panel_index.html'
#print('This template html is in directory: ', index_template)
upload_template = this_dir / 'templates/panel/panel_upload.html'
upload_success_template = this_dir / 'templates/panel/panel_upload_success.html'
display_image_template = this_dir / 'templates/panel/panel_display_image.html'
display_pdf_template = this_dir / 'templates/panel/panel_display_pdf.html'



# Create your views here.
def load_index(request):
    context = {
        "msg": f"This is the index page.",
    }
    return render(request, index_template, context)

def upload_success(request):
    context = {
        "msg": "File was uploaded successfully.",
    }
    return render(request, index_template, context)


def load_static_index(request):
    return HttpResponse("This is an index page.")



def upload_image(request, *args, **kwargs):
    if request.method == 'POST':
        form = ModelFormWithImageField(request.POST, request.FILES)
        if form.is_valid():            
            form.save()            
            return HttpResponseRedirect(reverse('panel:upload-success')) 
        else:
            print('form is not valid!')
    else:
        form = ModelFormWithImageField()

    context = {
        "form": form,  # todo: form need to be assigned to after Upload File button is clicked
    }
    return render(request, upload_template, context)

def upload_file(request, *args, **kwargs):
    #print("Http request method is: ", request.method)
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        """ 
         Just like normal form validation, model form validation is triggered implicitly when calling is_valid()
        """        
        if form.is_valid():
            """ 
            Every ModelForm also has a save() method. This method creates and saves a database object from the data bound to the form. A subclass of ModelForm can accept an existing model instance as the keyword argument instance; if this is supplied, save() will update that instance. If it’s not supplied, save() will create a new instance of the specified model:
            """
            form.save()
            """ 
            Prevents Resubmission: By redirecting, it prevents the form from being resubmitted if the user refreshes the page.
            """
            return HttpResponseRedirect(reverse('panel:upload-success')) 
        else:
            print('form is not valid!')
    else:
        form = ModelFormWithFileField()

    context = {
        "form": form,  
    }
    return render(request, upload_template, context)

def display_image(request, image_id, *args, **kwargs):
    # Get the specific image model object or raise a 404 error if not found
    img_mdl = get_object_or_404(ModelWithImageField, pk=image_id)    
    # Print the image name and URL for debugging purposes
    print(f"Image name: {img_mdl.image_name}, image.url: {img_mdl.image.url}")
    # Create context with the image model
    context = {
        "image_model": img_mdl,
    }    
    # Render the template with the context
    return render(request, display_image_template, context)

def display_image_old(request, image_id, *args, **kwargs):
    """ 
    img_mdls = ModelWithImageField.objects.all()
    for m in img_mdls:
        print(f"Image name: {m.image_name}, id: {m.id}") 
    """
    img_mdl = ModelWithImageField.objects.get(pk=image_id)
    print(f"image name: {img_mdl.image_name}, image.url: {img_mdl.image.url}")
    if img_mdl is not None:
        context = {
            "image_model": img_mdl,  
        }
        return render(request, display_image_template, context)
    else:
        raise Http404(f"Image {image_id} does not exist.")

def display_pdf(request, pdf_id, *args, **kwargs):
    # Get the specific image model object or raise a 404 error if not found
    pdf_mdl = get_object_or_404(ModelWithFileField, pk=pdf_id)    
    # Print the image name and URL for debugging purposes
    print(f"Pdf name: {pdf_mdl.file_name}, pdf.url: {pdf_mdl.file.url}")
    # Create context with the image model
    context = {
        "pdf_model": pdf_mdl,
    }    
    # Render the template with the context
    return render(request, display_pdf_template, context)