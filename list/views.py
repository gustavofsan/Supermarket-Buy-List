from math import prod
from socketserver import ThreadingUDPServer
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Product, ProductInRecipe, Recipe, Supermarket, SupermarketProduct
from django.db.models import F


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


def index(request):
    supermarkets = Supermarket.objects.all
    recipes = Recipe.objects.all
    context = {
        'supermarkets':supermarkets,
        'recipes':recipes
    }
    return render(request, 'index.html', context)


def request_all_itens(request):
    return get_all_itens_sup(request,1)
    #return JsonResponse(data)

def add_prod(request):
    if request.method == 'POST':
        newProd = Product(
            name = request.POST['name'],
            quantity = request.POST['quantity'],
            bought = (request.POST.get('bought', False)=="on"),
        )
        newProd.save()
        data = {
            "id": newProd.id,
        }
        #after inserting, add SupermarketProduct to each supermarket.
        supermarkets = Supermarket.objects.all()
        for sup in supermarkets:
            newSupProd = SupermarketProduct(
                place = "",
                price = 0,
                supermarket = sup,
                product = newProd,
            )
            newSupProd.save()

        return JsonResponse(data)
    return HttpResponse("Failed!")

def delete_prod(request,pk):
    if request.method == 'POST' or request.method=='GET':
        product = Product.objects.get(pk=pk)
        product.delete()
        return HttpResponse("Success!")
    return HttpResponse("Failed!")

def edit_prod(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        if 'name' in request.POST:
            product.name = request.POST['name']
        if 'quantity' in request.POST:
            product.quantity = request.POST['quantity']
        
        product.save()
        data = {
            "bought": product.bought,
        }
        if 'place' in request.POST:
            place = request.POST['place']
        if 'supermarket_id' in request.POST:
            supermarket_id = request.POST['supermarket_id']
            supermarketProduct = SupermarketProduct.objects.filter(supermarket__id=supermarket_id, product__id=product.id).update(place=place)

        return JsonResponse(data)
    return HttpResponse("Failed!")

def buy_prod(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        product.bought = not product.bought
        product.save()
        data = {
            "bought": product.bought,
        }
        return JsonResponse(data)
    return HttpResponse("Failed!")


def add_sup(request):
    if request.method == 'POST':
        newSup = Supermarket(
            name = request.POST['name'],
        )
        newSup.save()
        data = {
            "id": newSup.id,
        }
        return JsonResponse(data)
    return HttpResponse("Failed!")

def get_item_details(request):
    if request.method == 'POST':
        prod_id = request.POST['prod_id']
        supermarket_id = request.POST['supermarket_id']
        supermarketProduct = SupermarketProduct.objects.filter(supermarket__id=supermarket_id, product__id=prod_id)
        #print(supermarketProduct[0].place)
        data = {
            "place": supermarketProduct[0].place,
        }
        return JsonResponse(data)
    return HttpResponse("Failed!")

def get_all_itens_sup(request,pk):
    current_supermarket = pk
    products = SupermarketProduct.objects.filter(supermarket__id=current_supermarket)
    products_to_buy = products.filter(product__bought=False).values('price',
                                                                    'place',
                                                                    prodId=F('product__id'),
                                                                    name=F('product__name'),
                                                                    quantity=F('product__quantity'))
                                                                    
    products_bought = products.filter(product__bought=True).values('price',
                                                                    'place',
                                                                    prodId=F('product__id'),
                                                                    name=F('product__name'),
                                                                    quantity=F('product__quantity'))

    data = {
        "products_to_buy": list(products_to_buy),
        "products_bought": list(products_bought),
    }
    return JsonResponse(data)


def add_recipe(request):
    if request.method == 'POST':
        newRecipe = Recipe(
            name = request.POST['name'],
            time = request.POST['time'],
            serves = request.POST['serves'],
        )
        newRecipe.save()
        data = {
            "id": newRecipe.id,
        }
        return JsonResponse(data)
    return HttpResponse("Failed!")

def get_all_itens_recipe(request,pk):
    current_recipe = pk
    products = ProductInRecipe.objects.filter(recipe__id=current_recipe).values('quantity',
                                                                                prodId=F('product__id'), 
                                                                                name=F('product__name'),) 
                                                                                #talvez precise trazer mais dados
    print(products)
    data = {
        "products": list(products),
        #"products_to_buy": list(products_to_buy),
        #"products_bought": list(products_bought),
    }
    return JsonResponse(data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]