from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput
                               (attrs={'placeholder': 'Enter your first name'}))
    email = forms.CharField(max_length=100,
                            widget=forms.EmailInput
                            (attrs={'placeholder': 'Enter your email'}))
    
    password1  = forms.CharField(max_length=100,
                            widget=forms.PasswordInput
                            (attrs={'placeholder': 'Enter your password'}))

    password2 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput
                                (attrs={'placeholder': 'Confirm your password'}))
    class Meta:
        model = User
        fields =['username','email','password1','password2']






