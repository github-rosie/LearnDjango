from django.urls import path

from . import views

app_name = 'screen'

urlpatterns = [
    path(route='', view=views.index, name='index'),
]