from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from list import views



urlpatterns = [
    path('', include('list.urls')),
    
    path('admin/', admin.site.urls),
]
