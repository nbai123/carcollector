from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    horsepower = models.IntegerField()
    torque = models.IntegerField()
    ptwr = models.DecimalField(max_digits=4, decimal_places=2)
    cost = models.IntegerField()