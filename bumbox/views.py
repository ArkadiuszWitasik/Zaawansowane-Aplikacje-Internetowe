from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Count
from .forms import ArtistForm, TrackFormSet, AlbumForm, TrackForm, AlbumFilterForm
from .models import Artist, Album, Track
from django.core.paginator import Paginator


def home(request):
  return render(request, 'home.html')

def profile(request):
  return render(request, 'profile.html')

def login_user(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.success(request, "Błąd podczas logowania")
      return redirect('login-user')
  else:
    return render(request, 'authentication/login.html', {})

def logout_user(request):
  logout(request)
  return redirect('home')

def artists(request):
  artists = Artist.objects.all()

  p = Paginator(Artist.objects.all(), 3)
  page = request.GET.get('page')
  artists = p.get_page(page)

  return render(request, 'public/artists.html', {'artists': artists})

def show_artist(request, pk):
  artist = get_object_or_404(Artist, pk=pk)
  albums = artist.albums.all().prefetch_related('tracks')
  return render(request, 'public/artist_details.html', {'artist': artist, 'albums': albums})

def add_artist(request):
  subbmited = False

  if request.method == "POST":
    form = ArtistForm(request.POST or None, request.FILES or None)
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
  form = ArtistForm(request.POST or None, request.FILES or None, instance=artist)
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
  genre = request.GET.get('genre')
  albums = Album.objects.annotate(track_count=Count('tracks')).order_by("?")
  if genre:
    albums = albums.filter(genre__icontains=genre)
  return render(request, 'public/albums.html', {'albums': albums, 'form': AlbumFilterForm()})

def show_album(request, pk):
  album = get_object_or_404(Album, pk=pk)
  tracks = Track.objects.filter(album_id=pk)
  return render(request, 'public/album_details.html', {'album': album, 'tracks': tracks})

def add_album(request):
  if request.method == "POST":
    form = AlbumForm(request.POST, request.FILES)
    formset = TrackFormSet(request.POST)
    if form.is_valid() and formset.is_valid():
      album = form.save()
      tracks = formset.save(commit=False)
      for track in tracks:
        track.album = album
        track.save()
      return HttpResponseRedirect('/albums')
  else:
    form = AlbumForm()
    formset = TrackFormSet()
  return render(request, 'moderator/add_album.html', {'form': form, 'formset': formset})

def update_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = AlbumForm(request.POST or None, request.FILES or None, instance=album)

    if form.is_valid():
        form.save()

        return redirect(f'/albums/{album.id}')

    return render(request, 'moderator/update_album.html', {
        'album': album,
        'form': form,
    })

def add_track(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = TrackForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            track = form.save(commit=False)
            track.album = album
            track.save()
            return redirect(f'/albums/{album.id}')

    return render(request, 'moderator/add_track.html', {'album': album, 'form': form})

def delete_album(request, pk):
  album = get_object_or_404(Album, pk=pk)
  if request.method == "POST":
    album.delete()
    return HttpResponseRedirect('/albums')
  return render(request, 'moderator/delete_album.html', {'album': album})

def update_track(request, pk, pk2):
  album = get_object_or_404(Album, pk=pk)
  track = get_object_or_404(Track, pk=pk2)
  form = TrackForm(request.POST or None, instance=track)
  if form.is_valid():
    form.save()
    return redirect(f'/albums/{album.id}')

  return render(request, 'moderator/update_track.html', {'album': album, 'track': track, 'form': form})

def delete_track(request, pk, pk2):
  album = get_object_or_404(Album, pk=pk)
  track = get_object_or_404(Track, pk=pk2)
  if request.method == "POST":
    track.delete()
    return redirect(f'/albums/{album.id}')
  return render(request, 'moderator/delete_track.html', {'album': album, 'track': track})

def playlists(request):
  return render(request, 'playlists.html')
