from django import forms

from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'availability']
        labels = {  'name': 'Game name: ', 
                    'availability': 'Currently available? ',
                    'description': 'Description: '}
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}