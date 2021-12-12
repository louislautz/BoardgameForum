from django.shortcuts import redirect, render

from .models import Boardgamer, Game
from .forms import BoardgamerForm, GameForm

def index(request):
    """Home page for the BoardgameForum."""
    return render(request, 'main/index.html')


def games(request):
    """Shows all games"""
    games = Game.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'main/games.html', context)

def game(request, game_id):
    """Shows a specific game"""
    game = Game.objects.get(id = game_id)
    context = {'game': game}
    return render(request, 'main/game.html', context)

def new_game(request, boardgamer_id):
    """Adds a new game"""
    boardgamer = Boardgamer.objects.get(id = boardgamer_id)

    if request.method != 'POST':
        # No data submitted. Create a blank form.
        form = GameForm()
    else:
        # POST data submitted. Process data
        form = GameForm(data=request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = boardgamer
            new_game.save()
            return redirect('main:boardgamer', boardgamer_id=boardgamer_id)
        
    # Display a blank or invalid form
    context = {'boardgamer': boardgamer, 'form': form}
    return render(request, 'main/new_game.html', context)


def boardgamers(request):
    """Shows all boardgamers"""
    boardgamers = Boardgamer.objects.order_by('date_joined')
    context = {'boardgamers': boardgamers}
    return render(request, 'main/boardgamers.html', context)

def boardgamer(request, boardgamer_id):
    """Shows a specific boardgamer"""
    boardgamer = Boardgamer.objects.get(id = boardgamer_id)
    games = boardgamer.game_set.order_by('-date_added')
    context = {'boardgamer': boardgamer, 'games': games}
    return render(request, 'main/boardgamer.html', context)

def new_boardgamer(request):
    """Adds a new boardgamer"""
    if request.method != 'POST':
        # No data was submitted. Create a blank form
        form = BoardgamerForm()
    else:
        # POST data submitted; process data
        form = BoardgamerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:boardgamers')

    # Displays a blank or invalid form
    context = {'form': form}
    return render(request, 'main/new_boardgamer.html', context)