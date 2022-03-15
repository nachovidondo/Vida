from django.shortcuts import render
from .forms  import Contactform, JoinActivityForm
from . models import Activity, SubPlan
from django.core.mail import EmailMessage

from django.shortcuts import render,reverse , redirect
from django.urls import reverse_lazy
from datetime import timezone
import datetime
from datetime import datetime, timedelta
from django.views.generic.edit import  UpdateView

# Create your views here.

def index(request):
    return render (request, 'index.html')


#Contact
def contact(request):
    contact_form = Contactform()
  
    if request.method == "POST":
        contact_form = Contactform(data=request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name')
            email= request.POST.get('email')
            content= request.POST.get('content')
            """mail = EmailMessage(
                "vida Message : New Message Contact ",
                "From {} {}\n\n wrote :\n\n {}".format(name ,email,content),
                "vida.com", ["vida90@gmail.com"],-----> create a new email
                reply_to = [email]
                )"""
            try:
               """ mail.send() #Si esta todo ok redireccionar"""
               return redirect(reverse("automatic")+"?ok")



            except:
                return redirect(reverse("contacto")+"?fail")

    return render (request, 'contact.html', {'form':contact_form})


#Automatic message after contact us and book us
def automatic(request):
  
    return render (request, 'automatic.html')


#Suscriptions

def suscriptions(request):
    suscriptions = SubPlan.objects.all()
    return render (request, 'suscriptions.html', {'suscriptions': suscriptions})

def activities(request):
    
    now = datetime.now(timezone.utc)
    #Activities filter from now to the future
    activities = Activity.objects.filter(date_time__gte=now)
    return render (request, 'activity.html',{'activities' : activities})


