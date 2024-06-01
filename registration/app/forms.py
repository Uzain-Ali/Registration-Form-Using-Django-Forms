from django import forms 
from django.contrib.auth.forms import UserCreationForm,authenticate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields= ('username','email', 'first_name','last_name','password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField( max_length=100)
    password = forms.CharField( max_length=100)

    if username and password:
        user = authenticate( username=username, password=password)
        user.save()