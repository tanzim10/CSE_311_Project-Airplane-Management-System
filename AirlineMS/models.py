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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    status = models.CharField(max_length=2,choices =(('0','Pending'),('1','Confirmed'),('2','Cancelled')))
    date_created = models.DateTimeField(default= timezone.now)
    def __str__(self):
        return str(f"{self.flight.fl_code} - {self.user.first_name} {self.user.last_name}")


class FlightSchedule(models.Model):

    flight = models.ForeignKey(Flights, on_delete=models.CASCADE,primary_key=True)
    arr_time = models.TimeField()
    dept_time = models.TimeField()
    flight_date = models.DateTimeField()


