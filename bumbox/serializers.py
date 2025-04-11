from rest_framework import serializers
from .models import Album, Artist, Playlist, Profile, Track
from datetime import timedelta

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = ['id', 'name', 'description', 'picture']
    extra_kwargs = {
      'picture': {'required': False}
    }

class AlbumSerializer(serializers.ModelSerializer):
  artist = ArtistSerializer()
  class Meta:
    model = Album
    fields = ['id', 'title', 'artist', 'genre']
    extra_kwargs = {
      'picture': {'required': False}
    }

class TrackSerializer(serializers.ModelSerializer):
  album = AlbumSerializer()
  class Meta:
    model = Track
    fields = ['id', 'title', 'album', 'duration']

class PlaylistSerializer(serializers.ModelSerializer):
  tracks = TrackSerializer(many=True)
  total_duration = serializers.SerializerMethodField()
  average_duration = serializers.SerializerMethodField()
  shortest_track = serializers.SerializerMethodField()
  longest_track = serializers.SerializerMethodField()
  track_count = serializers.SerializerMethodField()

  class Meta:
    model = Playlist
    fields = ['id', 'name', 'profile', 'tracks', 'created_at', 'total_duration'
              , 'average_duration', 'longest_track', 'shortest_track', 'track_count']
    extra_kwargs = {
      'total_duration': {'required': False},
      'average_duration': {'required': False},
      'shortest_track': {'required': False},
      'longest_track': {'required': False},
      'track_count': {'required': False}
    }

  def get_total_duration(self, obj):
      return sum((track.duration for track in obj.tracks.all()), start=timedelta()).total_seconds()

  def get_average_duration(self, obj):
      tracks = obj.tracks.all()
      if tracks:
          return (sum((track.duration for track in tracks), start=timedelta()) / len(tracks)).total_seconds()
      return 0

  def get_shortest_track(self, obj):
      track = obj.tracks.order_by('duration').first()
      return track.duration.total_seconds() if track else None

  def get_longest_track(self, obj):
      track = obj.tracks.order_by('-duration').first()
      return track.duration.total_seconds() if track else None

  def get_track_count(self, obj):
      return obj.tracks.count()
