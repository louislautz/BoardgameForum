from django.contrib import admin
from django.contrib.auth import get_user_model

#from .models import Boardgamer
from .models import Game

Boardgamer = get_user_model()

#admin.site.register(User)
admin.site.register(Boardgamer)
admin.site.register(Game)