from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,ProfileForm,UserProfileUpdate,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


airline = [
    {
        'Name': 'Air Astra',
        'Airplane number': 'BX10231',
        'Type': 'AIRBUS A380',
        'Capacity': '200'
    },
    {
        'Name': 'West Jet',
        'Airplane number': 'CX10231',
        'Type': 'AIRBUS A350',
        'Capacity': '350'
    }

]


def home(request):
    info = {
        'info': airline
    }
    return render(request, 'AirlineMS/home.html', info)


def about(request):
    return render(request, 'AirlineMS/about.html')


def login(request):

    return render(request, 'AirlineMS/login.html',)


def register(response):
    form = CreateUserForm()
    profile = ProfileForm

    if response.method == 'POST':
        form = CreateUserForm(response.POST)
        if form.is_valid():
            user = form.save()
            messages.success(response, f'Your account has been created! You are able to Login.')
            return redirect('login')

    else:
        form = CreateUserForm()


    context = {'form': form,
               'profile':profile}
    return render(response, 'AirlineMS/register.html',context)

@login_required
def profile(response):


    return render(response, 'AirlineMS/profile.html')

@login_required
def profile_update(response):
    u_form = UserProfileUpdate(response.POST, instance=response.user)
    p_form = ProfileForm(response.POST, response.FILES, instance=response.user.profile)

    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(response, f'Your account has been updated!')
        return redirect('profile')

    else:
        u_form = UserProfileUpdate(instance=response.user)
        p_form = ProfileUpdateForm(instance=response.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(response,'AirlineMS/profile_update.html',context)




