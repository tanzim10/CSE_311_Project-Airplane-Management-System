from django.shortcuts import render , redirect
from .forms import CreateUserForm,ProfileForm,UserProfileUpdate,ProfileUpdateForm,SaveReservation,SaveRoute
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *




def home(request):
    airlines = Airlines.objects.all()
    airports = Airport.objects.all()
    flights = Flights.objects.all()
    context = {'airlines': airlines,
               'airports': airports,
               'flights':flights}

    return render(request,'AirlineMS/home.html',context)


def about(request):
    return render(request, 'AirlineMS/about.html')


def login(request):

    return render(request, 'AirlineMS/login.html')


def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are able to Login.')
            return redirect('login')

    else:
        form = CreateUserForm()


    context = {'form': form}

    return render(request, 'AirlineMS/register.html',context)

@login_required
def profile(response):

    return render(response, 'AirlineMS/profile.html')

@login_required
def profile_update(request):

    if request.method == 'POST':
        u_form = UserProfileUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserProfileUpdate(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,'AirlineMS/profile_update.html',context)


@login_required

def reservation(response):

    if response.method == 'POST':
        reserve = SaveReservation(response.POST)
        route = SaveRoute(response.POST)
        if reserve.is_valid() and route.is_valid():
            route = route.save()
            reserve = reserve.save()
            reserve.route = route
            reserve.user = response.user
            reserve.save()
            messages.success(response, f'Your Reservation has been completed!')
            return redirect('Air-home')

    else:
        reserve = SaveReservation()
        route = SaveRoute()

    context = {'route': route,
               'reserve':reserve}

    return render(response,'AirlineMS/reservation.html',context)


def search_flight(request):
    context = {}
    if request.method == 'POST':
        flying_from = request.POST['flying_from']
        flying_to = request.POST['flying_to']
        date = request.POST['departure_date']
        print(flying_from + "  " + flying_to + " " + date )
        flight_schedule = FlightSchedule.objects.filter(flight_date =date).values('flight')
        flight_list = [flight_id['flight'] for flight_id in flight_schedule]
        routes = Route.objects.filter(flight__id__in=flight_list, flying_from__contains=flying_from, flying_to__contains=flying_to)
        if routes:
            context = {'routes':routes,'dates':date}
        else:
            messages.warning(request, 'No Result Found.Search Again!')




    return render(request,'AirlineMS/search_flight.html',context)





@login_required
def view_reservation(request):
    reservations = Reservation.objects.filter(user=request.user)
    context = {'reservations':reservations}

    return render(request,'AirlineMS/view_reservation.html',context)





