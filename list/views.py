from math import prod
from socketserver import ThreadingUDPServer
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Product, Supermarket, SupermarketProduct
from django.db.models import F


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


def index(request):
    supermarkets = Supermarket.objects.all
    context = {
        'supermarkets':supermarkets
    }
    return render(request, 'index.html', context)


def request_all_itens(request):
    current_supermarket = 1
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
    print("CHEGOU AQUI")
    #return JsonResponse(True)
    return JsonResponse(data)

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
        if 'place' in request.POST:
            product.place = request.POST['place']
        product.save()
        data = {
            "bought": product.bought,
        }
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
        #return HttpResponse("Success!")
    return HttpResponse("Failed!")

def get_all_itens_sup(request,pk):
    products_to_buy = Product.objects.filter(bought=False).values()
    products_bought = Product.objects.filter(bought=True).values()
    print(products_to_buy)
    print(products_bought)

    data = {
        "products_to_buy": list(products_to_buy),
        "products_bought": list(products_bought),
    }
    print("CHEGOU AQUI")
    #return JsonResponse(True)
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