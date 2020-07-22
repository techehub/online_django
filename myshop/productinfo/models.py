from django.db import models

# Create your models here.

class Product (models.Model):
    name= models.CharField( max_length=100)
    description = models.CharField( max_length=250)
    price= models.IntegerField()
    brand= models.CharField(max_length=100, default="na")

    def __str__ (self):
        return str (self.id)   + " : " + self.name