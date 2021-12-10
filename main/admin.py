from django.contrib import admin

from .models import Boardgamer
from .models import Game

admin.site.register(Boardgamer)
admin.site.register(Game)