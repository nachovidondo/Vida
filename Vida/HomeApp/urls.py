from django import views
from django.urls import path

from HomeApp.models import Activity
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('automatic/', views.automatic, name="automatic"),
    path('suscriptions/', views.suscriptions, name ="suscriptions"),
    path('activities/', views.activities, name ="activities"),
   
]   