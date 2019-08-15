from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Game

def index(request):
    return render(request, 'game_streaming/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Your account was successfully created. Enjoy your stay!')
            user = form.save()
            login(request, user)
            return redirect('index')
    
    else:
        form = UserCreationForm()
    
    return render(request, 'game_streaming/register.html', {'form': form})

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_streaming/games_list.html', {'games': games})
