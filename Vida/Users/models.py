from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from  HomeApp.models import SubPlan, Activity
from django.contrib.auth.models import PermissionsMixin

from django.db.models.signals import post_save, post_delete


class UserManager(BaseUserManager):
    def create_user(self,email,username,name,surname,password=None):
        if not email:
            raise ValueError('The user must be a valid email')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,email,name,surname,password):
        user = self.create_user(
            email,
            username=username,
            name=name,
            surname=surname,
            password=password,
            )
        user.is_admin = True
        user.is_active=True
        user.save()
        return user


class User(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=200, blank=False, null=False, unique=True
    )
    email = models.EmailField(verbose_name="Email", unique=True)
    name = models.CharField(
        max_length=200, verbose_name="Name", blank=True, null=True
    )
    surname = models.CharField(
        max_length=200, verbose_name="Surname", blank=True, null=True
        )
    mobile = models.CharField(max_length=200, default= "----")
    subplan = models.ForeignKey(SubPlan, on_delete=models.CASCADE, default=1)
    status = models.BooleanField(default=True)
    
    creation_date = models.DateTimeField(auto_now=True, verbose_name="Date")
    image = models.ImageField(verbose_name="Image", upload_to='profile/', blank=True, null=True, default="profile.png")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    
    class Meta:
        verbose_name="User"
        verbose_name_plural="Users"
        
    #ATRIBUTE TO GET THE LOGIN
    USERNAME_FIELD = 'username'
    #FIELDS REQUIRED TO CREATE THE NEW USER
    REQUIRED_FIELDS = ['email', 'name','surname',]
    
    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    #is this user admin?
    @property
    def is_staff(self):
        return self.is_admin


class UserActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.activity.title + str(self.activity.date_time)


#Signal to control the number of clients in the activity
def activity_client_control(sender, instance, **kwargs):
    activity_title = instance.activity
    activity = Activity.objects.filter(id=activity_title.id).first()
    user_activity = UserActivity.objects.filter(activity=activity)
    users=user_activity.count()
    activity.quantity_of_clients=users
    activity.save()
    
post_save.connect(activity_client_control,sender=UserActivity)
post_delete.connect(activity_client_control,sender=UserActivity)
