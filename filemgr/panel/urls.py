from django.urls import path

from . import views

# Set path route urls
index_url = ''
upload_image_url = 'upload-image/'
upload_file_url = 'upload-file/'
upload_success_url = 'upload-success/'
display_image_url = 'display-image/<int:image_id>/'
display_pdf_url = 'display-pdf/<int:pdf_id>/'
display_table_url = 'display-table/'

# Set namespace for the app
app_name = 'panel'

urlpatterns = [
    path(route=index_url, view=views.load_index, name="index"),
    path(route=upload_image_url, view=views.upload_image, name="upload-image"),
    path(route=upload_file_url, view=views.upload_file, name="upload-file"),
    path(route=upload_success_url, view=views.upload_success, name="upload-success"),
    path(route=display_image_url, view=views.display_image, name="display-image"),
    path(route=display_pdf_url, view=views.display_pdf, name="display-pdf"),
    path(route=display_table_url, view=views.display_table, name="display-table"),
]