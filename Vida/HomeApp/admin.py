from django.contrib import admin

from . models import SubPlan, SubPlanFeature


@admin.register(SubPlan)
class SubPlanAdmin(admin.ModelAdmin):
    list_display=['title','price','status']

@admin.register(SubPlanFeature)
class SubPlanFeatureAdmin(admin.ModelAdmin):
    list_display=['title','subplan']
