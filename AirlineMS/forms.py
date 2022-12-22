from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone_number']


class UserProfileUpdate(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone_number']

class SaveReservation(forms.ModelForm):

    flight = forms.CharField(max_length=250)
    type = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    gender = forms.CharField(max_length=250)
    contact = forms.CharField(max_length=250)
    email = forms.CharField(max_length=250)
    address = forms.Textarea()


