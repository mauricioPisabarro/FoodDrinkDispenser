from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from food_drink_dispenser.models import DrinkLog, FoodLog, FoodDispenseRequest, DrinkDispenseRequest, RequestStatuses
from django.views.decorators.csrf import csrf_exempt


def index(request):
    template = loader.get_template('food_drink_dispenser/index.html')
    context = {}

    return HttpResponse(template.render(context, request))


def water_logs(request):
    template = loader.get_template('food_drink_dispenser/water_logs.html')
    waterLogList = DrinkLog.objects.all().order_by('-date')
    context = { 'waterLogList': waterLogList }   

    return HttpResponse(template.render(context, request))


def food_logs(request):
    template = loader.get_template('food_drink_dispenser/food_logs.html')
    foodLogList = FoodLog.objects.all().order_by('-date')
    context = { 'foodLogList': foodLogList }

    return HttpResponse(template.render(context, request))


def water_requests(request):
    template = loader.get_template('food_drink_dispenser/water_requests.html')
    waterRequestsList = DrinkDispenseRequest.objects.all().order_by('-date')
    
    context = { 'waterRequestsList': map(beautifyObject, waterRequestsList) }

    return HttpResponse(template.render(context, request))


def food_requests(request):
    template = loader.get_template('food_drink_dispenser/food_requests.html')
    foodRequestsList = FoodDispenseRequest.objects.all().order_by('-date')
    context = { 'foodRequestsList': map(beautifyObject, foodRequestsList) }

    return HttpResponse(template.render(context, request))


@csrf_exempt
def dispense_food(request):
    if request.method == 'POST':
        waterRequest = FoodDispenseRequest.objects.create()
        waterRequest.save()
        
        return redirect('food_requests') 
    
    template = loader.get_template('food_drink_dispenser/dispense_food.html')
    context = { }

    return HttpResponse(template.render(context, request))


@csrf_exempt
def dispense_water(request):
    if request.method == 'POST':
        waterRequest = DrinkDispenseRequest.objects.create()
        waterRequest.save()

        return redirect('water_requests')

    template = loader.get_template('food_drink_dispenser/dispense_water.html')
    context = { }

    return HttpResponse(template.render(context, request))


def beautifyObject(obj):
    if obj.status == RequestStatuses.FAILED:
        return {
            'date': obj.date,
            'status': 'FAILED',
        }
    elif obj.status == RequestStatuses.SUCCESSFUL:
        return {
            'date': obj.date,
            'status': 'SUCCESSFUL',
        }

    return {
        'date': obj.date,
        'status': 'PENDING',
    }