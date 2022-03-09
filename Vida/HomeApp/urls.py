from django import views
from django.urls import path

from HomeApp.models import Activity
from django.contrib.auth.decorators import login_required
from . views import contact , suscriptions,automatic, activities
from . views import index

urlpatterns = [
    path('', index, name="index"),
    path('contact/', login_required(contact), name="contact"),
    path('automatic/', login_required(automatic), name="automatic"),
    path('suscriptions/', login_required(suscriptions), name ="suscriptions"),
    path('activities/', login_required(activities), name ="activities"),
   
]   