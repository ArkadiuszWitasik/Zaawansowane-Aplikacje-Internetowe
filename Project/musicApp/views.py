from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from musicApp.forms import AlbumForm
from django.http import HttpResponse
from musicApp.models import Album, AlbumDetails, Track, Genre

def all(request):
  template = loader.get_template("musicApp/allAlbums.html")
  allAlbums = Album.objects.all()
  context = {'all_albums': allAlbums}
  return HttpResponse(template.render(context, request))

def details(request, album_id):
  template = loader.get_template("musicApp/albumDetail.html")
  album = Album.objects.get(id=album_id)
  albumDetails = AlbumDetails.objects.get(album=album_id)
  tracks = Track.objects.filter(album=album)
  genre = Genre.objects.filter(albums=album)
  context = {'album': album, 'albumDetails': albumDetails, 'tracks': tracks, 'genre': genre}

  return HttpResponse(template.render(context, request))

def addAlbum(request):
  form = AlbumForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect(all)
  return render(request, 'musicApp/addAlbumForm.html', {'newForm' : form})

def updateAlbum(request, album_id): 
  album = get_object_or_404(Album, pk=album_id)
  form = AlbumForm(request.POST or None, instance=album)
  if form.is_valid():
    form.save()
    return redirect(all)
  return render(request, 'musicApp/updateAlbum.html', {'updateForm': form})

def deleteAlbum(request, album_id):
  album = get_object_or_404(Album, pk=album_id)
  if request.method == "POST":
    album.delete()
    return redirect(all)
  return render(request, 'musicApp/deleteAlbum.html', {'album': album})