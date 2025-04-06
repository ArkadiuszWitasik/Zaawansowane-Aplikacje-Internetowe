from django import forms
from django.forms import ModelForm
from .models import Artist

class ArtistForm(ModelForm):
  class Meta:
    model = Artist
    fields = ('name', 'description', 'origin_country')
    labels = {
      'name': '',
      'description': '',
      'origin_country': '',
    }
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa'}),
      'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Opis'}),
      'origin_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kraj'}),
    }