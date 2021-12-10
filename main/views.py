from django.shortcuts import render

from .models import Boardgamer, Game

def index(request):
    """Home page for the BoardgameForum."""
    return render(request, 'main/index.html')

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