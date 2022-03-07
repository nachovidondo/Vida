from django.contrib import admin

from . models import SubPlan, SubPlanFeature, Activity


@admin.register(SubPlan)
class SubPlanAdmin(admin.ModelAdmin):
    list_display=['title','price','status']

@admin.register(SubPlanFeature)
class SubPlanFeatureAdmin(admin.ModelAdmin):
    list_display=['title','subplan']
    
    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display=['title', 'status','date_time']
