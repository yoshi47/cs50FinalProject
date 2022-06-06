from django.db import models

# Create your models here.

class LogModel(models.Model):
    start = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)
    people = models.IntegerField()
    days = models.IntegerField()
    result = models.IntegerField()
