from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


#CUSTOM LOGIN FORM
class LoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        
        def get_invalid_login_error(self):
            return forms.ValidationError(
                self.error_messages['invalid_login'],
                code = 'invalid_login',
                params = {'username':self.username_field.verbose_name}
            )
#CUSTOM USER FORM , TO REGISTER A NEW USER IN THE DATABASE
class UserForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter your password',
            'id':'password1',
            'required':'required'
        }
    ))
    password2 = forms.CharField(label="Password confirmation", widget = forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter your password again',
            'id':'password2',
            'required':'required'
        }
    ))
    class Meta:
        model = User
        fields = ('email','username','name','surname')
        widget = {
        'email':forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Correo electronico',
                }
            )
        },
        {
        'name':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your name',
                }
            )
        }, 
        {
        'surname':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your surname',
                }
            )
        },
        {
        'username':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your username',
                }
            )
        }, 
        def clean_password2(self):
            # BOTH PASSWORDS EQUAL?
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            if password1 != password2:
                raise forms.ValidationError('Password does not match')
            return password2
        