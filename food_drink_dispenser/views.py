from django.shortcuts import render
from django.http import HttpResponse
# from food_drink_dispenser.models import MODEL_NAME

def index(request):
    return HttpResponse('THIS IS THE INDEX')

def logs(request):
    return HttpResponse('SHOW LOGS')

def dispenser(request):
    return HttpResponse('SHOW LOGS')

# Create your views here.
# def sensor(request):
#     sensor = Sensor.objects.get(id=1)

#     return render(request, 'sensor.html', { 'sensor': sensor })