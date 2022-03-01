from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('automatic/', views.automatic, name="automatic"),
    path('suscriptions/', views.suscriptions, name ="suscriptions")
]   