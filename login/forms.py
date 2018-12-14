from django import forms
from login.models import User


class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget= forms.PasswordInput())

