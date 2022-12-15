from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,ProfileForm
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
            form.save()
            profile = CreateUserForm.objects.create(user=response.user)
            username = form.cleaned_data.get('username')
            messages.success(response, f'Your account has been created! You are able to Login.')
            profile.save()
            return redirect('login')

    else:
        form = CreateUserForm()


    context = {'form': form,
               'profile':profile}
    return render(response, 'AirlineMS/register.html',context)

@login_required
def profile(response):
    context = {'profile':profile}
    return render(response, 'AirlineMS/profile.html',context)



