from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('meetups/<slug:slug>/success', views.confirm_registration, name='confirm-registration'),
    path('meetups/<slug:slug>', views.meetup_details, name='meetup-detail'),
   
]