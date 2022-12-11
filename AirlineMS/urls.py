from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='Air-home'),
    path('about/',views.about,name = 'Air-about'),
    path('register/',views.register, name ='Air-register'),



]
