from django import forms
from .models import UploadedFile 


class UploadedFileForm(forms.Form):   
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    