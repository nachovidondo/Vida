from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView 
from .forms import LoginForm, AccountSettingsForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .models import User, UserActivity
from .forms import UserForm, UserActivityForm

from datetime import datetime ,timedelta, timezone

from HomeApp.models import Activity


#User Login
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
        
#User new account
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

#Logout
def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/')

#UserPlatform
def mysite(request): 
    now = datetime.now(timezone.utc)
    activity = Activity.objects.filter(date_time__gte=now).first()
    user_activities = UserActivity.objects.filter(user=request.user).filter(activity__title=activity.title)
    
    return render (request, 'mysite.html',{'user_activities': user_activities})

#User activity Join
class JoinActivity(CreateView):
    model = UserActivity
    form_class = UserActivityForm
    template_name = 'user_activity.html'
    
    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        user_id = self.request.user
        
        if form.is_valid():
            user = UserActivity(
                activity = form.cleaned_data.get('activity'),
                user= user_id)
            user.save()
            return redirect('automatic_activity')
        else:
            return render(request,self.template_name,{'form':form}) 

#Automatic Message
def automatic_activity(request):
    return render(request, 'automatic_activity.html')


class DeleteActivity(DeleteView):
    model = UserActivity
    success_url = reverse_lazy('mysite')

    

    