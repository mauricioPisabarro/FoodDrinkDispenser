from django.db import models

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

