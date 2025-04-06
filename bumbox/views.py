from django.shortcuts import render
from .forms import ArtistForm
from django.http import HttpResponseRedirect

def home(request):
  return render(request, 'home.html')

def profile(request):
  return render(request, 'profile.html')

def artists(request):
  return render(request, 'artists.html')

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