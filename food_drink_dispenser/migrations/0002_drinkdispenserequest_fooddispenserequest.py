# Generated by Django 2.2.6 on 2019-11-27 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_drink_dispenser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkDispenseRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodDispenseRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
