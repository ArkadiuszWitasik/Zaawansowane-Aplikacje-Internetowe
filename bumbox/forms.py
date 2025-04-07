from django import forms
from django.forms import ModelForm
from .models import Artist

class ArtistForm(ModelForm):
  class Meta:
    model = Artist
    fields = ('name', 'description', 'picture')
    labels = {
      'name': '',
      'description': '',
      'picture': '',
    }
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa'}),
      'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Opis', 'maxlength': 250}),
      # 'picture': forms.ImageField()
    }