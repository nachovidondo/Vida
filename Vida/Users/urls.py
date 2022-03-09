from django.urls import path
from django.contrib.auth  import views as auth_views 
from django.contrib.auth.decorators import login_required

from .views import JoinActivity, UserRegister, mysite, AccountSettings
from .views import MyActivities,automatic_activity, DeleteActivity


     

urlpatterns = [
     path('register/',UserRegister.as_view(), name='register'),
     path('reset_password/',
         auth_views.PasswordResetView.as_view(
              template_name='ResetPassword/password_reset.html'
              ),
         name='reset_password'
         ),
     path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
              template_name='ResetPassword/password_reset_sent.html'
              ),
         name='password_reset_done'),
     path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
              template_name='ResetPassword/password_reset_form.html'
              ), 
         name='password_reset_confirm'),
     path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
              template_name='ResetPassword/password_reset_done.html'
              ), 
         name='password_reset_complete'),
     path('mysite/', login_required(mysite), name="mysite"),
     path('account_settings/<int:pk>',login_required(AccountSettings.as_view()), 
         name='account_settings'),
     path('user_activity/',login_required(JoinActivity.as_view()), name="user_activity"),
     path('my_activities/',login_required(MyActivities.as_view()), name="my_activities"),
     path('automatic_activity',login_required(automatic_activity), name="automatic_activity"),
     path('delete_activity/<int:pk>',login_required( DeleteActivity.as_view()), 
          name='delete_activity'),
    ]