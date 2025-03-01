from django.db import models

class Album(modes.Model):
  title = models.CharField(max_length=64, blank=False, unique=False)
  author = models.CharField(max_length=64, blank=False, unique=False)
  genre = models.CharField(max_length=64, blank=False, unique=False)
  release_date = models.DateField(null=False, blank=False)
  # To be added later when new model Track will be aded
  # tracks = models.
  rating = models.DecimalField(max_digits=1, decimal_places=1, null=True, blank=True)
