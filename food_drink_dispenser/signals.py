from django.db.models.signals.pre_save import pre_save
from food_drink_dispenser.models import FoodLog, DrinkLog, FoodDispenseRequest, DrinkDispenseRequest

def pre_save_generic_handler(sender, instance, created, **kwargs):
    print('test')