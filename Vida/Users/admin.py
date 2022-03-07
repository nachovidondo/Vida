from django.contrib import admin
from . models import UserManager, User, UserActivity

# Register your models here.
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','username','surname','email','mobile','subplan','status',]
    search_fields = ['activity__title','activity__date_time','user__username']
    
    
@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display=['activity', 'user',]
    search_fields = ['activity__title','activity__date_time','user__username']