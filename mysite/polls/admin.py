
# we need to tell the admin that Question objects have an admin interface. To do this, open the polls/admin.py file, and edit it to look like this:
from django.contrib import admin
from .models import Question

# Register your models here.
admin.site.register(Question)

