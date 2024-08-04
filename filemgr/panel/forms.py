from django import forms

from . import models


""" 
django.forms.ModelForm:
- it represents an HTML form that can be used to create or update instances of a model.
- it automatically generates form fields based on the model's fields.
- it handles form validation and data cleaning. 
"""

class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = "__all__"

class ModelFormWithImageField(forms.ModelForm):
    class Meta:
        model = models.ModelWithImageField
        fields = "__all__"

class ModelFormWithFileField(forms.ModelForm):
    class Meta:
        model = models.ModelWithFileField
        fields = ['file_name', 'file']
    

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
