from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Artist, Album, Track

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
      'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
    }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'genre', 'picture']
        labels = {
            'title': '',
            'artist': '',
            'genre': '',
            'picture': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tytuł albumu'
            }),
            'artist': forms.Select(attrs={
                'class': 'form-control',
            }),
            'genre': forms.Select(attrs={
                'class': 'form-control',
            }),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'duration']
        labels = {
            'title': '',
            'duration': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tytuł utworu'
            }),
            'duration': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Czas trwania (MM:SS)'
            }),
        }

TrackFormSet = inlineformset_factory(
  parent_model=Album,
  model=Track,
  form=TrackForm,
  fields=('title', 'duration'),
  extra=5,
  can_delete=False,
)