from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from food_drink_dispenser.models import DrinkLog, FoodLog, FoodDispenseRequest, DrinkDispenseRequest
from django.views.decorators.csrf import csrf_exempt

# from polls.models import Sensor

def index(request):
    template = loader.get_template('food_drink_dispenser/index.html')
    context = {}

    return HttpResponse(template.render(context, request))


def water_logs(request):
    template = loader.get_template('food_drink_dispenser/water_logs.html')
    list_water = DrinkLog.objects.all()
    context = {
        'list_water': list_water
    }   

    return HttpResponse(template.render(context, request))


def food_logs(request):
    template = loader.get_template('food_drink_dispenser/food_logs.html')
    list_food = FoodLog.objects.all()
    context = {
        'list_food': list_food
    }

    return HttpResponse(template.render(context, request))

@csrf_exempt
def dispense_food(request):
    if request.method == 'POST':
        waterRequest = FoodDispenseRequest.objects.create()
        waterRequest.save()
    
    template = loader.get_template('food_drink_dispenser/dispense_food.html')
    context = { }

    return HttpResponse(template.render(context, request))

@csrf_exempt
def dispense_water(request):
    if request.method == 'POST':
        waterRequest = DrinkDispenseRequest.objects.create()
        waterRequest.save()

    template = loader.get_template('food_drink_dispenser/dispense_water.html')
    context = { }

    return HttpResponse(template.render(context, request))