from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Game
from .forms import GameForm

User = get_user_model()

def index(request):
    """Home page for the BoardgameForum."""
    return render(request, 'main/index.html')

@login_required
def games(request):
    """Shows all games"""
    games = Game.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'main/games.html', context)

@login_required
def game(request, game_id):
    """Shows a specific game"""
    game = Game.objects.get(id = game_id)
    context = {'game': game}
    return render(request, 'main/game.html', context)

@login_required
def new_game(request, User_id):
    """Adds a new game"""
    user = User.objects.get(id = User_id)

    if request.method != 'POST':
        # No data submitted. Create a blank form.
        form = GameForm()
    else:
        # POST data submitted. Process data
        form = GameForm(data=request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = user
            new_game.save()
            return redirect('users:profile', User_id=User_id)
        
    # Display a blank or invalid form
    context = {'user': user, 'form': form}
    return render(request, 'main/new_game.html', context)
