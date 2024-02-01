from django import forms
from .models import Movie

class MovieUpdate(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['description','image','year']