from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logs', views.logs, name='logs'),
    path('dispenser', views.dispenser, name='dispenser'),
]