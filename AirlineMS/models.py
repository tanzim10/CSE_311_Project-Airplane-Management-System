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
    airlines = models.ForeignKey(Airlines,on_delete=models.CASCADE, default ='')


class Airport(models.Model):
    air_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')), default=1)
    date_created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(f"{self.air_name}")


class Flights(models.Model):
    fl_code = models.CharField(max_length=100)
    duration = models.CharField(max_length=250)
    airline = models.ForeignKey(Airlines,on_delete=models.CASCADE)
    total_tickets = models.PositiveIntegerField(default=0, null =True)

    def __str__(self):
        return str(f"{self.fl_code}")

class Route(models.Model):

    route_no = models.AutoField(primary_key=True)
    flying_from = models.CharField(max_length=100, choices =(('DHK','DHK'),('CTG','CTG'),('CXB','CXB'),('JSR','JSR'),('SDP','SDP'),('BZL','BZL'),('SYL','SYL')),default='DHK')
    flying_to = models.CharField(max_length=100,choices =(('DHK','DHK'),('CTG','CTG'),('CXB','CXB'),('JSR','JSR'),('SDP','SDP'),('BZL','BZL'),('SYL','SYL')),default='CTG')
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)

    def __str__(self):
        return  str(f"{self.flying_from} to {self.flying_to} - {self.flight.fl_code}")



class Reservation(models.Model):

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
    number_of_tickets = models.CharField(max_length=100, choices=(('1','1'),('2','2'),('3','3'),('4','4')),default='1')
    route = models.ForeignKey(Route,on_delete=models.CASCADE,null =True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)




    def __str__(self):
        return str(f"{self.route.flight.fl_code} - {self.first_name} {self.last_name}")


class FlightSchedule(models.Model):

    flight = models.ForeignKey(Flights, on_delete=models.CASCADE,primary_key=True,related_name='flightschedule')
    arr_time = models.DateTimeField()
    dept_time = models.DateTimeField()
    flight_date = models.DateField()

    def __str__(self):
        return str(f"{self.flight.fl_code} -{self.flight_date}")


class Fare(models.Model):

    base = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    reservation = models.OneToOneField(Reservation,on_delete=models.CASCADE)




