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
    # Page that adds a new game to the database
    path('new_game/<int:user_id>/', views.new_game, name='new_game'),
    # Link that rents a game to a user
    path('games/rented/<int:game_id>/<int:user_id>', views.rentGame, name='rentGame'),
    # Link that returns a rented game
    path('games/return/<int:rent_id>', views.returnGame, name='returnGame'),
]