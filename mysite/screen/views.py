from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UploadedFileForm


# Create your views here.
def index(request):
    return HttpResponse('Hellow world!')


def upload_file(request):
    template_name = "screen/upload.html"
    form = UploadedFileForm()
    context = {"form": form}

    if request.method == 'POST':
        """ pass request.FILES into the forms constructor; this is how file data gets bound into a form."""
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect('/success/url')

    return render(request, template_name, context)




def handle_uploaded_file(f):
    with open("some/file/name.txt", "wb+") as destination:
        """Looping over UploadedFile.chunks() instead of using read() ensures that large files dont overwhelm your systems memory.
        """
        for chunk in f.chunks():
            destination.write(chunk)