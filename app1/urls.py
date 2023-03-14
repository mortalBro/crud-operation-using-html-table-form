from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('', views.fun,name='homepa'),
    path('home1', views.contact,name='homepage1'),
    path('send/', views.sendData,name='sendaction'),
    path('editt/<int:id>/', views.Edit,name='edit'),
    path('del/<int:id>/', views.Delete,name='delete'),
    path('create', views.createmethod,name='create'),
    path('update/<int:pk>/', views.updatemethod,name='update'),

]
