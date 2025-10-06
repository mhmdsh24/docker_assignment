from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['movie_title', 'actor1_name', 'actor2_name', 'director_name', 'movie_genre', 'release_year']
        widgets = {
            'movie_title': forms.TextInput(attrs={'class': 'form-control'}),
            'actor1_name': forms.TextInput(attrs={'class': 'form-control'}),
            'actor2_name': forms.TextInput(attrs={'class': 'form-control'}),
            'director_name': forms.TextInput(attrs={'class': 'form-control'}),
            'movie_genre': forms.TextInput(attrs={'class': 'form-control'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'movie_title': 'Movie Title',
            'actor1_name': 'Actor 1 Name',
            'actor2_name': 'Actor 2 Name',
            'director_name': 'Director Name',
            'movie_genre': 'Movie Genre',
            'release_year': 'Release Year',
        }
