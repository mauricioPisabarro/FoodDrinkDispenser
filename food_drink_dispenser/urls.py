from django.urls import path

from food_drink_dispenser.views import index, dispenser, FoodLogListView, DrinkLogListView

urlpatterns = [
    path('', index, name='index'),
    path('food-logs', FoodLogListView.as_view(), name='food_logs'),
    path('drink-logs', DrinkLogListView.as_view(), name='drink_logs'),
    path('dispenser', dispenser, name='dispenser'),
]