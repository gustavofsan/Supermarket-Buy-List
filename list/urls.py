from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('delete_prod/<str:pk>', views.delete_prod, name='delete_prod'),
    path('edit_prod/<str:pk>/', views.edit_prod, name='edit_prod'),
    path('buy_prod/<str:pk>/', views.buy_prod, name='buy_prod'),
    path('add_prod/', views.add_prod, name='add_prod'),
    path('request_all_itens/', views.request_all_itens, name='request_all_itens'),

    path('add_sup/', views.add_sup, name='add_sup'),
    path('get_all_itens_sup/<str:pk>/', views.get_all_itens_sup, name='get_all_itens_sup'),
]

