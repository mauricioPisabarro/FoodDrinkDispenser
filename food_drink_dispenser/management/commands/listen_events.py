from django.core.management.base import BaseCommand, CommandError
from food_drink_dispenser.models import FoodLog, DrinkLog
from django.db.models import signals
import paho.mqtt.client as mqtt

IS_TESTING_ON_PLAIN_LINUX = True
FOOD_TOPIC_SUBSCRIPTION = 'foodOutTopic'
WATER_TOPIC_SUBSCRIPTION = 'waterOutTopic'

FOOD_DISPENSE_CONFIRMATION_TOPIC_SUBSCRIPTION = 'foodConfirmationOutTopic'
WATER_DISPENSE_CONFIRMATION_TOPIC_SUBSCRIPTION = 'waterConfirmationOutTopic'

class Command(BaseCommand):
    def handle(self, *args, **options):
        client = mqtt.Client(client_id='mqtt-test')
        client.on_connect = on_connect
        client.on_message = on_message

        if IS_TESTING_ON_PLAIN_LINUX:
            client.connect('127.0.0.1', 1883, 60)
        else:
            client.username_pw_set('domotica', 'natdanv07')
            client.connect('127.0.0.1', port=1883)
        
        print('Connected to mosquitto successfully')
        client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print('LISTENER: Connected with result code: ' + str(rc))

    client.subscribe(FOOD_TOPIC_SUBSCRIPTION)
    client.subscribe(WATER_TOPIC_SUBSCRIPTION)
    client.subscribe(FOOD_DISPENSE_CONFIRMATION_TOPIC_SUBSCRIPTION)
    client.subscribe(WATER_DISPENSE_CONFIRMATION_TOPIC_SUBSCRIPTION)


def on_message(client, userdata, msg):
    topic = msg.topic
    data = msg.payload.decode('utf-8')

    if topic == FOOD_TOPIC_SUBSCRIPTION:
        print(FOOD_TOPIC_SUBSCRIPTION)
        print(data)
    elif topic == WATER_TOPIC_SUBSCRIPTION:
        print(WATER_TOPIC_SUBSCRIPTION)
        print(data)
    elif topic == FOOD_DISPENSE_CONFIRMATION_TOPIC_SUBSCRIPTION:
        print(FOOD_DISPENSE_CONFIRMATION_TOPIC_SUBSCRIPTION)
        print(data)
    elif topic == WATER_DISPENSE_CONFIRMATION_TOPIC_SUBSCRIPTION:
        print(WATER_DISPENSE_CONFIRMATION_TOPIC_SUBSCRIPTION)
        print(data)