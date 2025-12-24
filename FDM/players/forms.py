from django import forms
from .models import Player,Stats

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player 
        fields = '__all__'
        
        
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'age': 'Age',
            'height': 'Height (m)',
        }
        
        widgets = {
            'fname': forms.TextInput(attrs={'placeholder': 'e.g. Luka'}),
            'lname': forms.TextInput(attrs={'placeholder': 'e.g. Modric'}),
            'age': forms.NumberInput(attrs={'placeholder': 'e.g. 38'}),
            'height': forms.NumberInput(attrs={'placeholder': 'e.g. 1.72'})
        }
        
        
class StatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = '__all__'

        labels = {
            'player': 'Player',
            'position': 'Position',
            'team': 'Team',
            'goals': 'Goals Scored',
            'rating': 'Rating',
        }

        widgets = {
            'player': forms.Select(attrs={'class': 'form-select'}),
            'position': forms.TextInput(attrs={'placeholder': 'e.g. Midfielder'}),
            'team': forms.TextInput(attrs={'placeholder': 'e.g. Real Madrid'}),
            'goals': forms.NumberInput(attrs={'placeholder': 'e.g. 7'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'e.g. 8.5'}),
        }


