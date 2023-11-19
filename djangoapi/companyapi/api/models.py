from django.db import models
from django.utils import timezone

class Device(models.Model):
    uid = models.CharField(max_length=50, unique=True)  
    name = models.CharField(max_length=100) 

class TemperatureReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)  # Relation to Device model
    temperature = models.FloatField()  # Temperature data
    timestamp = models.DateTimeField(default=timezone)  
    # Timestamp when the reading was added

class HumidityReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)  # Relation to Device model
    humidity = models.FloatField()  # Humidity data
    timestamp = models.DateTimeField(default=timezone)  # Timestamp when the reading was added 

# class Reading(models.Model):
#     device = models.ForeignKey(Device, on_delete=models.CASCADE)
#     parameter = models.CharField(max_length=255)
#     value = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)