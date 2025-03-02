from django.forms import ModelForm
from musicApp.models import Album

class AlbumForm(ModelForm):
  class Meta:
    model = Album
    fields = ['title', 'author']