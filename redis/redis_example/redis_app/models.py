from django.db import models

# Create your models here.

class Recepi(models.Model):
    name = models.CharField(max_length=100)
    decription = models.TextField()
    image = models.CharField(max_length=400)

    def __str__(self):
        return self.name