from django.shortcuts import render

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
  return render(request, 'moderator/add_artist.html')