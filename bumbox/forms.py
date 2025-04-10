from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Artist, Album, Track, Profile, Playlist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class AlbumFilterForm(forms.ModelForm):
   class Meta:
      model = Album
      fields = ['genre']
      labels = {
         'genre': ''
      }
      widgets = {
         'genre': forms.Select(attrs={
            'class': 'form-control'
         })
      }

class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(required=True, max_length=250, widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Kilka słów o sobie...'
    }))
    favourite_genre = forms.ChoiceField(choices=[
    ('POP', 'Pop'),
    ('ROCK', 'Rock'),
    ('RAP', 'Rap'),
    ('OTHER', 'Other')
    ],widget=forms.Select(attrs={
        'class': 'form-control', 'placeholder': ''
    }))
    class Meta:
      model = User
      fields = ['username', 'password1', 'password2', 'bio', 'favourite_genre']
    def save(self, commit=True):
       user = super().save(commit)
       profile, created = Profile.objects.get_or_create(user=user)
       profile.bio = self.cleaned_data['bio']
       profile.favourite_genre = self.cleaned_data['favourite_genre']
       profile.save()
       return user

class PlaylistForm(forms.ModelForm):
    class Meta:
       model = Playlist
       fields = ['name', 'tracks']
       labels = {'name': '', 'tracks': ''}
       widgets = {
          'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa playlisty'}),
          'tracks': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'height: 500px;'}),
          }

TrackFormSet = inlineformset_factory(
  parent_model=Album,
  model=Track,
  form=TrackForm,
  fields=('title', 'duration'),
  extra=5,
  can_delete=False,
)