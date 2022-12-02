from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='Air Astra'),
    path('about/',views.about, name='Air Astra-about')


]
