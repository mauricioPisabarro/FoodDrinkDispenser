from django.apps import AppConfig
from django.db.models.signals.pre_save import pre_save

class FoodDrinkDispenserConfig(AppConfig):
    name = 'food_drink_dispenser'

    def ready(self):
        from .models import FoodDispenseRequest, DrinkDispenseRequest
        from .signals import pre_save_dispense_food_handler, pre_save_dispense_drink_handler

        pre_save.connect(pre_save_dispense_food_handler, sender=FoodDispenseRequest)
        pre_save.connect(pre_save_dispense_drink_handler, sender=DrinkDispenseRequest)
