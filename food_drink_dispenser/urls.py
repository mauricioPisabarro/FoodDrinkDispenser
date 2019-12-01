from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('water_logs/', views.water_logs, name='water_logs'),
    path('food_logs/', views.food_logs, name='food_logs'),
    path('water_requests/', views.water_requests, name='water_requests'),
    path('food_requests/', views.food_requests, name='food_requests'),
    path('dispense_food/', views.dispense_food, name='dispense_food'),
    path('dispense_water/', views.dispense_water, name='dispense_water'),
]