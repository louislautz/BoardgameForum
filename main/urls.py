"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all games 
    path('games/', views.games, name='games'),
    # Page that shows a specific game
    path('games/<int:game_id>', views.game, name='game'),
    # Page that shows all boardgamers
    path('boardgamers/', views.boardgamers, name='boardgamers'),
    # Page that shows a specific game
    path('boardgamers/<int:boardgamer_id>', views.boardgamer, name='boardgamer'),
]