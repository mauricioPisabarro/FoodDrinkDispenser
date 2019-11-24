from django.apps import AppConfig


class FoodDrinkDispenserConfig(AppConfig):
    name = 'food_drink_dispenser'

    def ready(self):
        from .models import PizzaFoodLog, DrinkLog, FoodDispenseRequest, DrinkDispenseRequest
        from .signals import pizza_saved_handler
        post_save.connect(pizza_saved_handler, sender=Pizza)
