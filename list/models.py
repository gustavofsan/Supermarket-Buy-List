from unittest.util import _MAX_LENGTH
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    bought = models.BooleanField()
    place = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('place',)



class Supermarket(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class SupermarketRow(models.Model):
    place = models.CharField(max_length=100)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.place