from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('email', views.email, name='sendEmail'),
    path('verifyView', views.verifyView, name='verifyView'),
    path('verify', views.verify, name='verify'),
    path('verifyGood', views.verifyGood, name='verifyGood'),
]