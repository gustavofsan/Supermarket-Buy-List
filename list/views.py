from math import prod
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Product


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


def index(request):
    products = None
    #products = Product.objects.all

    false_and_true = {False, True}
    context = {'products':products,
                'false_and_true':false_and_true,
    }
    return render(request, 'index.html', context)


def request_all_itens(request):
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

def add_prod(request):
    if request.method == 'POST':
        newProd = Product(
            name = request.POST['name'],
            quantity = request.POST['quantity'],
            bought = (request.POST.get('bought', False)=="on"),
            place = request.POST['place']
        )
        newProd.save()
        data = {
            "id": newProd.id,
        }
        return JsonResponse(data)
        #return HttpResponse("Success!")
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