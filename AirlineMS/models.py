from django.db import models
from django.conf import settings
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser, User


class User(AbstractUser):

    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_no = PhoneField(blank = True, help_text = 'Contact Phone Number')
    email_v = models.ForeignKey(to = settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

