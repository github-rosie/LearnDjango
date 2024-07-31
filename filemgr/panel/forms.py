from django import forms

from .models import ModelWithImageField, ModelWithFileField


""" 
django.forms.ModelForm:
- it represents an HTML form that can be used to create or update instances of a model.
- it automatically generates form fields based on the model's fields.
- it handles form validation and data cleaning. 
"""

class ModelFormWithImageField(forms.ModelForm):
    class Meta:
        model = ModelWithImageField
        fields = "__all__"


class ModelFormWithFileField(forms.ModelForm):
    class Meta:
        model = ModelWithFileField
        fields = ['file_name', 'file']
    

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
