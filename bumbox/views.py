from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.db.models import Count
from .forms import ArtistForm, TrackFromSet, AlbumForm
from .models import Artist, Album, Track

def home(request):
  return render(request, 'home.html')

def profile(request):
  return render(request, 'profile.html')

def artists(request):
  artists = Artist.objects.all()
  return render(request, 'public/artists.html', {'artists': artists})

def show_artist(request, pk):
  artist = get_object_or_404(Artist, pk=pk)
  albums = artist.albums.all().prefetch_related('tracks')
  return render(request, 'public/artist_details.html', {'artist': artist, 'albums': albums})

def add_artist(request):
  subbmited = False

  if request.method == "POST":
    form = ArtistForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/add_artist?subbmited=True')
  else:
    form = ArtistForm
    if 'subbmited' in request.GET:
      subbmited = True

  return render(request, 'moderator/add_artist.html', {'form': form, 'subbmited': subbmited})

def update_artist(request, pk):
  artist = get_object_or_404(Artist, pk=pk)
  form = ArtistForm(request.POST or None, instance=artist)
  if form.is_valid():
    form.save()
    return redirect(f'/artists/{artist.id}')
  return render(request, 'moderator/update_artist.html', {'artist': artist, 'form': form})

def delete_artist(request, pk):
  artist = get_object_or_404(Artist, pk=pk)
  if request.method == "POST":
    artist.delete()
    return HttpResponseRedirect('/artists')
  return render(request, 'moderator/delete_artist.html', {'artist': artist})

def albums(request):
  albums = Album.objects.annotate(track_count=Count('tracks'))
  return render(request, 'public/albums.html', {'albums': albums})

def show_album(request, pk):
  album = get_object_or_404(Album, pk=pk)
  tracks = Track.objects.filter(album_id=pk)
  return render(request, 'public/album_details.html', {'album': album, 'tracks': tracks})

def add_album(request):
  if request.method == "POST":
    form = AlbumForm(request.POST, request.FILES)
    formset = TrackFromSet(request.POST)
    if form.is_valid() and formset.is_valid():
      album = form.save()
      tracks = formset.save(commit=False)
      for track in tracks:
        track.album = album
        track.save()
      return HttpResponseRedirect('/albums')
  else:
    form = AlbumForm()
    formset = TrackFromSet()
  return render(request, 'moderator/add_album.html', {'form': form, 'formset': formset})

def update_album(request, pk):
  return render(request, 'moderator/update_album.html')

def delete_album(request, pk):
  album = get_object_or_404(Album, pk=pk)
  if request.method == "POST":
    album.delete()
    return HttpResponseRedirect('/albums')
  return render(request, 'moderator/delete_album.html', {'album': album})

def playlists(request):
  return render(request, 'playlists.html')
