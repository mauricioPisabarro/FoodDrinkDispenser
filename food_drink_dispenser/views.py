from django.shortcuts import render
from django.http import HttpResponse
# from polls.models import Sensor

def index(request):
    return HttpResponse('THIS IS THE INDEX')

# Create your views here.
# def sensor(request):
#     sensor = Sensor.objects.get(id=1)

#     return render(request, 'sensor.html', { 'sensor': sensor })