from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='file_index'),
    path('fileView', views.fileView, name='fileView'),
    path('file', views.upload, name='fileUpload'),
]