from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Pokemon
import bcrypt

def home(request):
    return render(request, 'userHTML/home.html')

def catchThePokemon(request):
    user = User.objects.get(id = request.session['id'])
    context = {
        'collector': user,
        'pokemon': Pokemon.objects.all(),
        'pagetitle': f"{user.username}'s Catch Page!"
    }
    return render(request, 'userHTML/catch.html', context)

# USER REGISTRATION AND LOGIN
def handle_registration(request):
    if request.method == 'POST':
        if not User.objects.filter(username = request.POST['username']):
            preHash = request.POST['password']
            hash_n_salt = bcrypt.hashpw(preHash.encode(), bcrypt.gensalt(7)).decode()
            newUser = User.objects.create(
                username = request.POST['username'],
                password = hash_n_salt,
            )
            request.session['userid'] = newUser.id
            request.session['username'] = newUser.username
            request.session['loggedin'] = True
            messages.success(f'Whoop, whoop, {newUser.username}! You have successfully signed up to catch some Pokemon!')
            return redirect('catch')
        pass
    else:
        return redirect('home')

def handle_login(request):
    if request.method == 'POST':
        pass
    else:
        return redirect('home')

def handle_logout(request):
    pass