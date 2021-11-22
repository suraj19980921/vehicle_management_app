from django.db import models

# Create your models here.

class Vehicle(models.Model):
    name = models.CharField(max_length=256)
    camera1 = models.ImageField(null=True, blank=True)
    camera2 = models.ImageField(null=True, blank=True)
    speed = models.IntegerField()
    average_speed = models.FloatField()
    temperature = models.FloatField()
    fuel_level = models.FloatField()
    engine_status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    