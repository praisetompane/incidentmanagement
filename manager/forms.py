from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from manager.models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('personnelNumber', 'idNumber', 'cellphone', 'residence', 'roomNumber')


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintananceRequest
        fields = ('type', 'status', 'description', 'picture')
