from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import LoginForm, AccountSettingsForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .models import User
from .forms import UserForm


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('mysite')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    
    def dispatch(self,request,*args, **kwargs):
        #USER AUTHENTICADED -> MYSITE
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        
        #USER NOT AUTHENTICADED ->LOGIN AGAIN
        else:
     
            return super(Login,self).dispatch(request,*args,**kwargs)
    
    def form_valid(self,form):
        #SAVE THE USER
        login(self.request,form.get_user())

       
        return super(Login,self).form_valid(form)
        

class UserRegister(CreateView):
    model = User
    form_class = UserForm
    template_name = 'register.html'
    def post(self,request,*args, **kwargs):
        # METHOD TO SAVE THE PASSWORD ENCRIPTED
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            new_user = User(
                email = form.cleaned_data.get('email'),
                username = form.cleaned_data.get('username'),
                name = form.cleaned_data.get('name'),
                surname = form.cleaned_data.get('surname'),
                image = form.cleaned_data.get('image')
                )
            new_user.set_password(form.cleaned_data.get('password1'))
            new_user.save()
            return redirect('login')
        else:
            return render(request,self.template_name,{'form':form}) 


#Edit Profile Photo
class AccountSettings(UpdateView):
    model = User
    form_class =  AccountSettingsForm
    template_name = 'account_settings.html'
    success_url= reverse_lazy('mysite')


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/')

def mysite(request): 
 
    return render (request, 'mysite.html')


 