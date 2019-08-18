from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Game, UserLibraryGame, GameImage, GameContainer
from .container import start_game_container

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
    current_containers = request.user.containers.filter(is_in_use=True)
    current_game = None
    if current_containers:
        current_game = current_containers[0].image.game
    return render(request, 'game_streaming/user_library.html',
            {'games': user_games, 'current_game': current_game})

@login_required
def user_library_add_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if not request.user.games.filter(game__id=game_id):
        user_game = UserLibraryGame(user=request.user, game=game)
        user_game.save()
        messages.success(request, '{} is now added to your games.'.format(game.name))
    
    return redirect('user_library')

@login_required
def user_library_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.user.games.filter(game__id=game_id):
        # Todo check if another game is running
        current_containers = request.user.containers.filter(is_in_use=True, image__game=game)
        is_current_game = not not current_containers
        return render(request, 'game_streaming/game_details_library.html',
                {'game': game, 'is_current_game': is_current_game})
    else:
        messages.error(request, '{} is not in your games.'.format(game.name))
    
    return redirect('user_library')

@login_required
def run_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.user.games.filter(game__id=game_id):
        # Todo check if another game is running
        container = start_game_container(game, request.user)
        if container:
            container.save()
            # Todo game streaming
            return render(request, 'game_streaming/container_info.html',
                    {'container': container})
        else:
            messages.error(request, 'Error, cannot launch {}.'.format(game.name))
    else:
        messages.error(request, '{} is not in your games.'.format(game.name))
    
    return redirect('user_library')
