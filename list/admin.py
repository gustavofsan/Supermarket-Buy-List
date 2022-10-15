from django.contrib import admin
from list.models import Product,Supermarket, SupermarketProduct, Recipe, ProductInRecipe

# Register your models here.
admin.site.register(Product)
admin.site.register(Supermarket)
admin.site.register(SupermarketProduct)
admin.site.register(Recipe)
admin.site.register(ProductInRecipe)
