from django.urls import path

from . import views

index_url = ''
upload_image_url = 'upload-image/'
upload_url = 'upload/'
upload_sucess_url = 'upload-success/'


app_name = 'panel'

urlpatterns = [
    path(route=index_url, view=views.load_index, name="panel_index"),
    path(route=upload_image_url, view=views.upload_image, name="upload_image"),
    path(route=upload_url, view=views.upload_file, name="upload"),
    path(route=upload_sucess_url, view=views.load_index, name="upload_success"),
]