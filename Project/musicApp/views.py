from django.shortcuts import render
from django.http import HttpResponse
from musicApp.models import Album

def all(request):
  albums = Album.objects.all()
  html = "<h1>Lista albumów</h1><ul>"
  for album in albums:
    html += f"<li>{album.title} - {album.author} - {album.genre} - {album.release_date} - {album.rating}</li>"
  html += "</ul>"
  return HttpResponse(html)

def details(request, album_id):
  album = Album.objects.get(id=album_id)
  html = f"""<h1>{album.title}</h1>
                      <ul>
                      <li>Autor: {album.author}</li>
                      <li>Typ: {album.genre}</li>
                      <li>Data wydania: {album.release_date}</li>
                      <li>Ocena: {album.rating}</li>
                      </ul>"""
  return HttpResponse(html)