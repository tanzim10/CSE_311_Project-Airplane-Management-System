from django.shortcuts import render , redirect
from .forms import CreateUserForm,ProfileForm,UserProfileUpdate,ProfileUpdateForm,SaveReservation,SaveRoute
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *




def home(request):
    airlines = Airlines.objects.all()
    airports = Airport.objects.all()
    context = {'airlines': airlines,
               'airports': airports}
    return render(request,'AirlineMS/home.html',context)


def about(request):
    return render(request, 'AirlineMS/about.html')


def login(request):

    return render(request, 'AirlineMS/login.html')


def register(response):
    profile = ProfileForm

    if response.method == 'POST':
        form = CreateUserForm(response.POST)
        if form.is_valid():
            form.save()
            profile.save()
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


@login_required

def reservation(response):

    if response.method == 'POST':
        reserve = SaveReservation(response.POST)
        route = SaveRoute(response.POST)
        if reserve.is_valid() and route.is_valid():
            reserve.save()
            route.save()
            messages.success(response, f'Your Reservation has been completed!')
            return redirect('Air-home')

    else:
        reserve = SaveReservation()
        route = SaveRoute()

    context = {'route': route,
               'reserve':reserve}

    return render(response,'AirlineMS/reservation.html',context)




