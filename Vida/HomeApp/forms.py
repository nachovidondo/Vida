from django import forms
from django.forms.widgets import TextInput

from HomeApp.models import Activity




#CONTACT FORM

class Contactform(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Name'}
    ))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Email'}
    ))
    content = forms.CharField(required= True, widget=forms.Textarea(
        attrs={"rows":5, "cols":20, 'class':'form-control','placeholder':'Message'}
    ))



#Form to Join the user in actvity

class JoinActivityForm(forms.ModelForm):
  class Meta:
        model = Activity
        fields = ['users']
      