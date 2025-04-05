from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  nickname = models.CharField(max_length=50, blank=False)
  bio = models.TextField(blank=True)

class Artist(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  origin_country = models.CharField(max_length=50, blank=True)

class Album(models.Model):
  title = models.CharField(max_length=200)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')

class Track(models.Model):
  title = models.CharField(max_length=200)
  album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
  duration = models.DurationField()
  genre = models.CharField(max_length=50, choices=[
    ('POP', 'Pop'),
    ('ROCK', 'Rock'),
    ('RAP', 'Rap'),
    ('OTHER', 'Other')
  ])

class Playlist(models.Model):
  name = models.CharField(max_length=100)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='playlists')
  tracks = models.ManyToManyField(Track, related_name='playlists')
  created_at = models.DateTimeField(auto_now_add=True)