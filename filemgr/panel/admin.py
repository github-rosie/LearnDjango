# panel.admin.py 
from django.contrib import admin

# Register your models here.
from .models import ModelWithImageField, ModelWithFileField

""" 
The admin.site.register() function in Django is used to register a model with the Django admin site. Registering a model with the admin site allows you to manage the model through the Django admin interface, which includes creating, updating, deleting, and listing records of that model. 
"""
admin.site.register(ModelWithImageField)
admin.site.register(ModelWithFileField)