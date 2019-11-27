# Generated by Django 2.2.6 on 2019-11-27 14:51

from django.db import migrations, models
import food_drink_dispenser.models


class Migration(migrations.Migration):

    dependencies = [
        ('food_drink_dispenser', '0002_drinkdispenserequest_fooddispenserequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkdispenserequest',
            name='status',
            field=models.IntegerField(choices=[(1, 'PENDING'), (2, 'SUCCESSFUL'), (3, 'FAILED')], default=food_drink_dispenser.models.RequestStatuses(1)),
        ),
        migrations.AddField(
            model_name='fooddispenserequest',
            name='status',
            field=models.IntegerField(choices=[(1, 'PENDING'), (2, 'SUCCESSFUL'), (3, 'FAILED')], default=food_drink_dispenser.models.RequestStatuses(1)),
        ),
    ]
