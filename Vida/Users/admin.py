from django.contrib import admin
from . models import UserManager, User, UserActivity

# Register your models here.

admin.site.register(User)

    
@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display=['activity', 'user',]