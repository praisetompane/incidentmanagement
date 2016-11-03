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
        labels = {
            'username': 'User Name',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'password': 'Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}),
        }
        help_texts = {
            'username': '',  # Hack to remove the default message
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('personnelNumber', 'idNumber', 'cellphone', 'residence', 'roomNumber')
        labels = {
            'personnelNumber': 'Personnel Number',
            'idNumber': 'ID Number',
            'cellphone': 'Cell Phone',
            'residence': 'Residence',
            'roomNumber': 'Room Number'
        }
        widgets = {
            'personnelNumber': forms.TextInput(attrs={'class': 'form-control', 'name': 'personnelNumber'}),
            'idNumber': forms.NumberInput(attrs={'class': 'form-control', 'name': 'idNumber'}),
            # TODO Add ID validation on front end
            'cellphone': forms.NumberInput(attrs={'class': 'form-control', 'name': 'cellphone'}),
            'residence': forms.Select(attrs={'class': 'form-control', 'name': 'residence'}),
            'roomNumber': forms.TextInput(attrs={'class': 'form-control', 'name': 'roomNumber'}),
        }


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintananceRequest
        fields = ('type', 'status', 'description', 'picture')
        labels = {
            'type': 'Maintenance Type',
            'status': 'Status',
            'description': 'Description',
            'picture': 'Picture',
        }
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control', 'name': 'type'}),
            'status': forms.Select(attrs={'class': 'form-control', 'name': 'status'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'name': 'description'}),
            'picture': forms.FileInput(attrs={'class': 'form-control', 'name': 'picture'}),
        }



        # Cutomise the widgets for bootstrap?
