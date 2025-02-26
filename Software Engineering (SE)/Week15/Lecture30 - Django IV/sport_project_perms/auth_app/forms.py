# auth_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User	 # This is a default table for the database


class UserRegisterForm(UserCreationForm):   # RegisterForm is inheriting from UserCreationForm
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
