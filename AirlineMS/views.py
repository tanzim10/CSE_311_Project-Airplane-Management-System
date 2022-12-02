from django.shortcuts import render
from django.http import HttpResponse

airline = [
    {
        'Name' :'Air Astra',
        'Airplane number' : 'BX10231',
        'Type' : 'AIRBUS A380',
        'Capacity':'200'
    },
    {
        'Name' :'West Jet',
        'Airplane number' : 'CX10231',
        'Type' : 'AIRBUS A350',
        'Capacity':'350'
    }

]


def home(request):
    info = {
        'info' : airline
    }
    return render(request, 'AirlineMS/home.html',info)

def about(request):
    return render(request,'AirlineMS/about.html')



