from django.shortcuts import render

def home(request):
    return render(request, 'userHTML/home.html')
