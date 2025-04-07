from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('artists', views.artists, name='artists'),
    path('artists/<int:pk>/', views.show_artist, name="artist-details"),
    path('albums', views.albums, name='albums'),
    path('playlists', views.playlists, name='playlists'),
    path('add_artist', views.add_artist, name='add-artist'),
]
