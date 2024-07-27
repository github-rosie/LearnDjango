from django.urls import path

from . import views


app_name = 'panel'

urlpatterns = [
    path(route="", view=views.index_view_static, name="index"),
    path(route="hello-world/", view=views.hello_world_view, name="hello world"),
    path(route="hello/", view=views.hello_world_view, name="hello"),
    path(route="hello-world.html", view=views.hello_world_view, name="hello world html"),
]