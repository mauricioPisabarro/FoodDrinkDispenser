from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from food_drink_dispenser.models import FoodLog, DrinkLog, FoodDispenseRequest, DrinkDispenseRequest

class FoodLogListView(ListView):

    model = FoodLog
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DrinkLogListView(ListView):

    model = DrinkLog
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def index(request):
    return HttpResponse('THIS IS THE INDEX')

def dispenser(request):
    return HttpResponse('SHOW LOGS')

# Create your views here.
# def sensor(request):
#     sensor = Sensor.objects.get(id=1)

#     return render(request, 'sensor.html', { 'sensor': sensor })