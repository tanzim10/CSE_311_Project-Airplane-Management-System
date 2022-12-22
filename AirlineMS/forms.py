from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


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

    class Meta:
        model = Reservation
        fields = ['flight', 'first_name', 'last_name', 'gender', 'contact', 'email', 'address',]


    def clean_flight(self):
        fid = self.cleaned_data['flight']
        try:
            flight = Flights.objects.get(id =fid)
            return flight
        except:
            raise forms.ValidationError(f"Invalid Flight")







