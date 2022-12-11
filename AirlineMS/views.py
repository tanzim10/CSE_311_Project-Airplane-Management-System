from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

    if response.method =='POST':
        form = CreateUserForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(response, f'Your account has been created! You are able to Login.')
            return redirect('login')

    else:
        form = CreateUserForm()


    context = {'form': form}
    return render(response, 'AirlineMS/register.html',context)

@login_required
def profile(response):

    return render(response, 'AirlineMS/profile.html')


