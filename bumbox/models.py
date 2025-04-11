from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(blank=True, max_length=250)
  favourite_genre = models.CharField(max_length=50, blank=True, choices=[
    ('POP', 'Pop'),
    ('ROCK', 'Rock'),
    ('RAP', 'Rap'),
    ('OTHER', 'Other')
  ])

  def __str__(self):
    return self.user.username

class Artist(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=False, max_length=250)
  picture = models.ImageField(upload_to='images/', blank=True)

  def __str__(self):
    return self.name

class Album(models.Model):
  title = models.CharField(max_length=200)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
  genre = models.CharField(max_length=50, blank=False, choices=[
    ('POP', 'Pop'),
    ('ROCK', 'Rock'),
    ('RAP', 'Rap'),
    ('OTHER', 'Other')
  ])
  picture = models.ImageField(blank=True, upload_to='images/')

  def __str__(self):
    return self.title

class Track(models.Model):
  title = models.CharField(max_length=200, blank=False)
  album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
  duration = models.DurationField(blank=False)

  def __str__(self):
    return self.title

class Playlist(models.Model):
  name = models.CharField(max_length=100, blank=False)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='playlists')
  tracks = models.ManyToManyField(Track, related_name='playlists')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name