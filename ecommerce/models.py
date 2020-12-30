from django.db import models
from django.contrib.auth.models import User


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.CharField(max_length=255)
    lat = models.FloatField()
    long = models.FloatField()
    country = models.CharField(max_length=255)
    postcode = models.CharField(max_length=32)
    address = models.TextField()
