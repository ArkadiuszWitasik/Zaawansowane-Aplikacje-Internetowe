from django.template import loader
from django.http import HttpResponse
from musicApp.models import Album

def all(request):
  template = loader.get_template("musicApp/allAlbums.html")
  allAlbums = Album.objects.all()
  context = {'all_albums': allAlbums}
  return HttpResponse(template.render(context, request))

def details(request, album_id):
  template = loader.get_template("musicApp/albumDetail.html")
  album = Album.objects.get(id=album_id)
  context= {'album': album}
  return HttpResponse(template.render(context, request))