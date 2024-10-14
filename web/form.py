from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupform(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)

    class meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')