from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.username} Profile'


class Airlines(models.Model):
    a_name = models.CharField(max_length = 250)
    status = models.CharField(max_length=2, choices= (('1','Active'),('2','Inactive')), default =1)
    date_created = models.DateTimeField(auto_now=True)



    def __str__(self):
        return str(f"{self.a_name}")


class Airplanes(models.Model):
    airplane_name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    max_seats = models.IntegerField(default=0)


class Airport(models.Model):
    air_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')), default=1)
    date_created = models.DateTimeField(auto_now=True)
    airplane = models.ManyToManyField(Airplanes)


    def __str__(self):
        return str(f"{self.air_name}")


class Flights(models.Model):
    fl_code = models.CharField(max_length=100)
    duration = models.CharField(max_length=250)
    airline = models.ForeignKey(Airlines,on_delete=models.CASCADE)



class Reservation(models.Model):

    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    status = models.CharField(max_length=2,choices =(('0','Pending'),('1','Confirmed'),('2','Cancelled')))
    date_created = models.DateTimeField(default= timezone.now)
    ticket_no = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=10,choices=(('Male','Male'),('Female','Female')), default='Male')
    first_name = models.CharField(max_length=250,null =True)
    last_name = models.CharField(max_length=250,null =True)
    gender = models.CharField(max_length=50, choices=(('Male', 'Male'), ('Female', 'Female')), default='Male')
    email = models.CharField(max_length=250,null=True)
    contact = models.CharField(max_length=250,null =True)
    address = models.CharField(max_length=250,null=True)




    def __str__(self):
        return str(f"{self.flight.fl_code} - {self.user.first_name} {self.user.last_name}")


class FlightSchedule(models.Model):

    flight = models.ForeignKey(Flights, on_delete=models.CASCADE,primary_key=True)
    arr_time = models.DateTimeField()
    dept_time = models.DateTimeField()
    flight_date = models.DateTimeField()

class Route(models.Model):

    route_no = models.IntegerField()
    flying_from = models.CharField(max_length=100)
    flying_to = models.CharField(max_length=100)
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)


class Fare(models.Model):

    base = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    reservation = models.OneToOneField(Reservation,on_delete=models.CASCADE)

class Passenger(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    dob = models.DateTimeField()




