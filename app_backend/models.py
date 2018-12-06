from django.contrib.auth.models import User
from django.db import models


class Farm(models.Model):
    uuid = models.CharField(max_length=10, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    sensor_temp_air = models.PositiveIntegerField(default=0)
    sensor_temp_water = models.PositiveIntegerField(default=0)
    sensor_light = models.PositiveIntegerField(default=0)
    last_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uuid


class History(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='history')
    sensor_temp_air = models.PositiveIntegerField(default=0)
    sensor_temp_water = models.PositiveIntegerField(default=0)
    sensor_light = models.PositiveIntegerField(default=0)
    date = models.DateTimeField()

    def __str__(self):
        return '%s - %s' % (self.farm, self.date)
