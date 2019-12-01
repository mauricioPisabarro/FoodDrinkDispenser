from django.db import models
from django.db.models.signals import post_save
import paho.mqtt.client as mqtt
from enum import IntEnum

IS_TESTING_ON_PLAIN_LINUX = True

DRINK_TOPIC = 'waterInTopic'
FOOD_TOPIC = 'foodInTopic'

class RequestStatuses(IntEnum):
    PENDING = 1
    SUCCESSFUL = 2
    FAILED = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class FoodLog(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class DrinkLog(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class FoodDispenseRequest(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.IntegerField(choices=RequestStatuses.choices(), default=RequestStatuses.PENDING)

class DrinkDispenseRequest(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.IntegerField(choices=RequestStatuses.choices(), default=RequestStatuses.PENDING)

def post_save_dispense_food_handler(sender, instance, created, **kwargs):
    client = getMQTTClient()
    client.publish(FOOD_TOPIC)

def post_save_dispense_drink_handler(sender, instance, created, **kwargs):
    client = getMQTTClient()
    client.publish(DRINK_TOPIC)


def getMQTTClient():
    client = mqtt.Client(client_id='mqtt-test')

    if IS_TESTING_ON_PLAIN_LINUX:
        client.connect('127.0.0.1', 1883, 60)
    else:
        client.username_pw_set('domotica', 'natdanv07')
        client.connect('127.0.0.1', port=1883)

    return client


post_save.connect(post_save_dispense_food_handler, sender=FoodDispenseRequest)
post_save.connect(post_save_dispense_drink_handler, sender=DrinkDispenseRequest)
