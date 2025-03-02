from django.db import models

class Album(models.Model):
  title = models.CharField(max_length=64, blank=False, unique=False)
  author = models.CharField(max_length=64, blank=False, unique=False)

  def __str__(self):
    return f'{self.title} | {self.author}'
  
class AlbumDetails(models.Model):
  album = models.OneToOneField(Album, on_delete=models.CASCADE, primary_key=True)
  release_date = models.DateField(null=False, blank=False)
  rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
  major = models.CharField(max_length=64, blank=False, unique=False)

  def __str__(self):
    return f'{self.album.title} | {self.release_date} | {self.rating} | {self.major}'

class Track(models.Model):
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  title = models.CharField(max_length=64, blank=False, unique=False)
  duration = models.CharField(max_length=20, blank=False, unique=False)

  def __str__(self):
    return f'{self.album.title} | {self.title} | {self.duration}'

class Genre(models.Model):
  albums = models.ManyToManyField(Album)
  name = models.CharField(max_length=64, blank=False, unique=False)

  def __str__(self):
    return f'{self.albums} | {self.name}'