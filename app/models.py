from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.name