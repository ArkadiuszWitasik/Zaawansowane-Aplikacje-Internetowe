from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ArtistForm
from .models import Artist

def home(request):
  return render(request, 'home.html')

def profile(request):
  return render(request, 'profile.html')

def artists(request):
  artists = Artist.objects.all()
  return render(request, 'artists.html', {'artists': artists})

def albums(request):
  return render(request, 'albums.html')

def playlists(request):
  return render(request, 'playlists.html')

def add_artist(request):
  subbmited = False

  if request.method == "POST":
    form = ArtistForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/add_artist?subbmited=True')
  else:
    form = ArtistForm
    if 'subbmited' in request.GET:
      subbmited = True

  return render(request, 'moderator/add_artist.html', {'form': form, 'subbmited': subbmited})