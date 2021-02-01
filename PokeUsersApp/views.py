from django.shortcuts import render
from .models import User, Pokemon

def home(request):
    return render(request, 'userHTML/home.html')
