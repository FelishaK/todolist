from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('delete/<int:pk>/', delete, name='delete'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]