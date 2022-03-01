from django.shortcuts import render
from .forms  import Contactform

from django.core.mail import EmailMessage

from django.shortcuts import render,reverse , redirect

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
                "vida.com", ["vida90@gmail.com"],
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