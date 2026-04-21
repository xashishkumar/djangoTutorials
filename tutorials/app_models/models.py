from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=10)
    model = models.CharField(max_length=10)
    price = models.IntegerField()

def __str__(self):
        return self.name
