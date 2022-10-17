from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_prod/<str:pk>', views.delete_prod, name='delete_prod'),
    path('edit_prod/<str:pk>/', views.edit_prod, name='edit_prod'),
    path('buy_prod/<str:pk>/', views.buy_prod, name='buy_prod'),
    path('add_prod/', views.add_prod, name='add_prod'),
    path('request_all_itens/', views.request_all_itens, name='request_all_itens'),
    
    path('get_item_details/', views.get_item_details, name='get_item_details'),

    path('add_sup/', views.add_sup, name='add_sup'),
    path('get_all_itens_sup/<str:pk>/', views.get_all_itens_sup, name='get_all_itens_sup'),

    
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('get_all_itens_recipe/<str:pk>/', views.get_all_itens_recipe, name='get_all_itens_recipe'),
    path('add_prod_to_recipe/', views.add_prod_to_recipe, name='add_prod_to_recipe'),
    
    path('add_recipe_to_buyList/', views.add_recipe_to_buyList, name='add_recipe_to_buyList'),
    path('get_items_to_add_in_recipe/', views.get_items_to_add_in_recipe, name='get_items_to_add_in_recipe'),

]

