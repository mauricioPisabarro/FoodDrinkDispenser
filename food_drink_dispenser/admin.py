from django.contrib import admin
from food_drink_dispenser.models import FoodLog, DrinkLog, FoodDispenseRequest, DrinkDispenseRequest

admin.site.register(FoodLog)
admin.site.register(DrinkLog)
admin.site.register(FoodDispenseRequest)
admin.site.register(DrinkDispenseRequest)