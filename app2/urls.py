from django.contrib import admin
from django.urls import path
from app2 import views
urlpatterns = [
    path('hom', views.index,name='hompage'),
]
