from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='Air-home'),
    path('about/',views.about,name = 'Air-about'),
    path('login/',views.login, name ='Air-login'),
    path('register',views.register, name ='Air-register'),



]
