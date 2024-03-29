from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='carsindex'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
]