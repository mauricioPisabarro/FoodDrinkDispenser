from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# from polls.models import Sensor

def index(request):
    template = loader.get_template('food_drink_dispenser/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def water_logs(request):
    template = loader.get_template('food_drink_dispenser/water_logs.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def food_logs(request):
    template = loader.get_template('food_drink_dispenser/food_logs.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def dispense_food(request):
    template = loader.get_template('food_drink_dispenser/dispense_food.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def dispense_water(request):
    template = loader.get_template('food_drink_dispenser/dispense_water.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

# Create your views here.
# def sensor(request):
#     sensor = Sensor.objects.get(id=1)

#     return render(request, 'sensor.html', { 'sensor': sensor })