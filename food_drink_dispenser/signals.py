from django.db.models.signals.pre_save import pre_save

def pre_save_dispense_food_handler(sender, instance, created, **kwargs):
    print('test')

def pre_save_dispense_drink_handler(sender, instance, created, **kwargs):
    print('test')