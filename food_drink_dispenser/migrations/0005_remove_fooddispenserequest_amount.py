# Generated by Django 2.2.6 on 2019-12-01 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_drink_dispenser', '0004_auto_20191129_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooddispenserequest',
            name='amount',
        ),
    ]