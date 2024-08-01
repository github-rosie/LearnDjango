from django.urls import path

from . import views

index_url = ''
upload_image_url = 'upload-image/'
upload_file_url = 'upload-file/'
upload_success_url = 'upload-success/'
display_image_url = 'display-image/<int:image_id>/'


app_name = 'panel'

urlpatterns = [
    path(route=index_url, view=views.load_index, name="index"),
    path(route=upload_image_url, view=views.upload_image, name="upload-image"),
    path(route=upload_file_url, view=views.upload_file, name="upload-file"),
    path(route=upload_success_url, view=views.upload_success, name="upload-success"),
    path(route=display_image_url, view=views.display_image, name="display-image"),
]