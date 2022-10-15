from itertools import product
from unittest.util import _MAX_LENGTH
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    bought = models.BooleanField()

    def __str__(self):
        return self.name

    #class Meta:
    #    ordering = ('place',)

class Supermarket(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class SupermarketProduct(models.Model):
    place = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.name+ " - " + self.supermarket.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    serves = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class ProductInRecipe(models.Model):
    product = models.ForeignKey(Product,  null=True, on_delete=models.SET_NULL)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.IntegerField()