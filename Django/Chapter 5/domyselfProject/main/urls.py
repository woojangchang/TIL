from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index', views.index, name='main_index'),
    path('error', views.error, name='main_error'),
    path('index/download/', views.download, name='main_download'),
    path('login', views.login, name='main_login'),
    path('logout/', views.logout, name='main_logout'),
]