from django.core.management.base import BaseCommand, CommandError
from food_drink_dispenser.models import FoodLog, DrinkLog, FoodDispenseRequest, DrinkDispenseRequest
from django.db.models import signals

class Command(BaseCommand):
    def miFuncion(self):
        print('MI FUNCION')

    def handle(self, *args, **options):
        print('holamunfo')