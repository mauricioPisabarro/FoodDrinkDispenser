from django.db import models, signals

class FoodLog(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField()

class DrinkLog(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField()

class FoodDispenseRequest(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField()

class DrinkDispenseRequest(models.Model):
    models.IntegerField(default=0)
    date = models.DateTimeField()


def pre_save_dispense_food_handler(sender, instance, created, **kwargs):
    print('test')

def pre_save_dispense_drink_handler(sender, instance, created, **kwargs):
    print('test')
