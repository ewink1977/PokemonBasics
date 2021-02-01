from typing import ItemsView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('catch', views.catchThePokemon, name = 'catch'),
    path('register', views.handle_registration, name = 'register'),
    path('login', views.handle_login, name = 'login'),
    path('logout', views.handle_logout, name = 'logout'),
]