from django.db import models, signals
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
    date = models.DateTimeField()

class DrinkLog(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField()

class FoodDispenseRequest(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField()
    status = models.IntegerField(choices=RequestStatuses.choices(), default=RequestStatuses.PENDING)

class DrinkDispenseRequest(models.Model):
    models.IntegerField(default=0)
    date = models.DateTimeField()
    status = models.IntegerField(choices=RequestStatuses.choices(), default=RequestStatuses.PENDING)

def pre_save_dispense_food_handler(sender, instance, created, **kwargs):
    client = getMQTTClient()
    # client.publish(FOOD_TOPIC, 'MESSAGE')

def pre_save_dispense_drink_handler(sender, instance, created, **kwargs):
    client = getMQTTClient()
    # client.publish(DRINK_TOPIC, 'MESSAGE')


def getMQTTClient():
    client = mqtt.Client(client_id='mqtt-test')

    if IS_TESTING_ON_PLAIN_LINUX:
        client.connect('127.0.0.1', 1883, 60)
    else:
        client.username_pw_set('domotica', 'natdanv07')
        client.connect('127.0.0.1', port=1883)

    return client
