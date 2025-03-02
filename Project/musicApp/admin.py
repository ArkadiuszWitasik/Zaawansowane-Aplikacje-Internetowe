from django.contrib import admin
from musicApp.models import Album, AlbumDetails, Track, Genre

admin.site.register(Album)
admin.site.register(AlbumDetails)
admin.site.register(Track)
admin.site.register(Genre)