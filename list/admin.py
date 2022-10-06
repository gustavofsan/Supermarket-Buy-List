from django.contrib import admin
from list.models import Product,Supermarket, SupermarketProduct

# Register your models here.
admin.site.register(Product)
admin.site.register(Supermarket)
admin.site.register(SupermarketProduct)