from django.db import models
from django.contrib.auth.models import User


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



class Airport(models.Model):
    air_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')), default=1)
    date_created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(f"{self.air_name}")

    
class Airplanes(models.Model):
    airplane_name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    max_seats = models.IntegerField(default=0)


    def __str__(self):
        return str(f'{self.airplane_name}')


class Flights(models.Model):
    fl_code = models.CharField(max_length=100)
    duration = models.CharField(max_length=250)














