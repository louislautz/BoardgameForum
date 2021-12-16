from django.contrib import admin

from .models import Game, Rent

class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'availability']
    list_filter = ['availability']
    search_fields = ['name']
    ordering = ['-availability']

class RentAdmin(admin.ModelAdmin):
    list_display = ['game', 'renter', 'returned']
    list_filter = ['returned']
    search_fields = ['game__name']
    ordering = ['returned']

admin.site.register(Game, GameAdmin)
admin.site.register(Rent, RentAdmin)