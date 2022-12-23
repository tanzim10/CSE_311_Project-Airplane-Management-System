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

    flight = forms.ModelChoiceField(queryset= Flights.objects.all(), empty_label='Select a Flight', blank=True)

    class Meta:
        model = Reservation
        fields = ['flight', 'first_name', 'last_name', 'gender', 'contact', 'email', 'address','number_of_tickets']
        exclude =['flight_id']




class SaveRoute(forms.ModelForm):

    class Meta:
        model = Route
        fields = ['flying_from','flying_to']
        exclude = ['route_no']





