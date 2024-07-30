from django.urls import path

from . import views


app_name = 'panel'

urlpatterns = [
    path(route="", view=views.load_index, name="index"),
    path(route="upload-image", view=views.upload_image, name="upload image"),
    path(route="upload-file", view=views.upload_file, name="upload file"),
    
    #path(route="upload_image", view=views.upload_image_view, name="upload image"),

 
]