from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Game, UserLibraryGame

def index(request):
    return render(request, 'game_streaming/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account was successfully created. Enjoy your stay!')
            return redirect('index')
    
    else:
        form = UserCreationForm()
    
    return render(request, 'game_streaming/register.html', {'form': form})

def market(request):
    games = Game.objects.all()
    owned_games_ids = []
    if request.user.is_authenticated:
        owned_games_ids = [user_game.game.id for user_game in request.user.games.all()]
    
    return render(request, 'game_streaming/market.html',
            {'games': games, 'owned_games_ids': owned_games_ids})

@login_required
def user_library(request):
    user_games = request.user.games.all()
    return render(request, 'game_streaming/user_library.html', {'games': user_games})

@login_required
def user_library_add_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if not request.user.games.filter(game__id=game_id):
        user_game = UserLibraryGame(user=request.user, game=game)
        user_game.save()
        messages.success(request, '{} is now added to your games.'.format(game.name))
    
    return redirect('user_library')

