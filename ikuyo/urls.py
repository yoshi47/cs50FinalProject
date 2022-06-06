from django.urls import path

from . import views

urlpatterns = [
    path('', views.TravelEstimate, name='travel_estimate'),
]
