from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Pokemon
import bcrypt

def home(request):
    return render(request, 'userHTML/home.html')

def catchThePokemon(request):
    if not request.session['loggedin'] == True:
        messages.error(request, f"D'oh!! You have to be logged in to access this page. How else can we keep track of your kick ass collection?", extra_tags = 'danger')
        return redirect('home')
    user = User.objects.get(id = request.session['userid'])
    context = {
        'collector': user,
        'pokemon': Pokemon.objects.all(),
        'pagetitle': f"{user.username}'s Catch Page!"
    }
    return render(request, 'userHTML/catch.html', context)

# THIS IS A GET REQUEST FOR THE SAKE OF SIMPLICITY.
def addPokemon(request, pokeID):
    user = User.objects.get(id = request.session['userid'])
    if not Pokemon.objects.filter(poke_id = pokeID):
        pokemon2add = Pokemon.objects.create(
            poke_id = pokeID
        )
        user.pokemon_captured.add(pokemon2add)
        context = {
        'collector': user,
        'pokemon': Pokemon.objects.all(),
        'pagetitle': f"{user.username}'s Catch Page!"
    }
        messages.success(request, f"Nice work! You've added Pokemon number {pokeID} to your collection!")
        return render(request, 'userHTML/partial.html', context)
    else:
        pokemon2add = Pokemon.objects.get(poke_id = pokeID)
        user.pokemon_captured.add(pokemon2add)
        context = {
        'collector': user,
        'pokemon': Pokemon.objects.all(),
        'pagetitle': f"{user.username}'s Catch Page!"
    }
        messages.success(request, f"Nice work! You've added Pokemon number {pokeID} to your collection!")
        return render(request, 'userHTML/partial.html', context)

def displayPokemon(request):
    user = User.objects.get(id = request.session['userid'])
    context = {
        'collector': user,
        'pokemon': Pokemon.objects.all(),
        'pagetitle': f"{user.username}'s Catch Page!"
    }
    return render(request, 'userHTML/partial.html', context)

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
            messages.success(request, f'Whoop, whoop, {newUser.username}! You have successfully signed up to catch some Pokemon!')
            return redirect('catch')
        else:
            dupUser = request.POST['username']
            messages.error(request, f'OMG!!! {dupUser} is aready in use. Please choose a different user name!', extra_tags = 'danger')
            return redirect('home')
    else:
        return redirect('home')

def handle_login(request):
    if request.method == 'POST':
        userSearch = User.objects.filter(username = request.POST['username'])
        if userSearch:
            user = userSearch[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['userid'] = user.pk
                request.session['username'] = user.username
                request.session['loggedin'] = True
                messages.success(request, f"ALRIGHT {user.username}!!! You have successfully logged in! Now, let's catch some Pokemon!")
                return redirect('catch')
            else:
                messages.error(request, "Hrm... That password didn't work. If you're a hacker, please knock that off, otherwise try again or sign up for a new account!", extra_tags = 'danger')
                return redirect('home')
        else:
            messages.error(request, "Weird. I didn't find that username in the database. Have you signed up? Did you typo? Please try again!", extra_tags = 'danger')
            return redirect('home')
    else:
        return redirect('home')

def handle_logout(request):
    del request.session['userid']
    del request.session['username']
    request.session['loggedin'] = False
    messages.success(request, "Thanks for stopping by! You've been logged off, but I know you'll be back!")
    return redirect('pokeall')