# panel.admin.py 
from django.contrib import admin

# Register your models here.
from .models import ModelWithImageField, ModelWithFileField


class ModelwithFileAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

""" 
The admin.site.register() function in Django is used to register a model with the Django admin site. Registering a model with the admin site allows you to manage the model through the Django admin interface, which includes creating, updating, deleting, and listing records of that model. 

Pass in ModelwithFileAdmin as argument for register() function is to display ID of the model in admin
"""

admin.site.register(ModelWithImageField, ModelwithFileAdmin)  
admin.site.register(ModelWithFileField, ModelwithFileAdmin) 