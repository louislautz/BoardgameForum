from django import forms

from .models import Boardgamer, Game

class BoardgamerForm(forms.ModelForm):
    class Meta:
        model = Boardgamer
        fields = ['username', 'biography']
        labels = {'username': 'Username: ', 'biography': 'Description: '}

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'availability']
        labels = {  'name': 'Game name: ', 
                    'availability': 'Currently available? ',
                    'description': 'Description: '}
        widgets = {'description': forms.Textarea(attrs={'cols': 500})}