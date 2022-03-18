from django.db import models


# Suscription Plan
class SubPlan(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    

# Suscription plan features
class SubPlanFeature(models.Model):
    subplan = models.ForeignKey(SubPlan, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    
class Activity(models.Model):
    title = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    status = models.BooleanField(default=False)
    quantity_of_clients = models.IntegerField(default = 0)
    
    users = models.ManyToManyField("Users.User", related_name="User",blank=True,null=True)
    
    def __str__(self):
        return self.title + " " + str(" - " )+ str(self.date_time)
    