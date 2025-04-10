from rest_framework import serializers
from .models import Album, Artist, Playlist, Profile, Track

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = ['id', 'name', 'description', 'picture']

class AlbumSerializer(serializers.ModelSerializer):
  class Meta:
    model = Album
    fields = ['id', 'title', 'artist', 'genre']

class TrackSerializer(serializers.ModelSerializer):
  class Meta:
    model = Track
    fields = ['id', 'title', 'album', 'duration']

class PlaylistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Playlist
    fields = ['id', 'name', 'profile', 'tracks', 'created_at']

