from django.urls import path

from . import views


app_name = 'panel'

urlpatterns = [
    path(route="", view=views.index_view, name="index"),
    path(route="upload_file", view=views.upload_file_view, name="upload file"),
    path(route="upload_image", view=views.upload_image_view, name="upload image"),

    path(route="hello-world/", view=views.hello_world_view, name="hello world"),
    path(route="hello/", view=views.hello_world_view, name="hello"),
    path(route="hello-world.html", view=views.hello_world_view, name="hello world html"),
]