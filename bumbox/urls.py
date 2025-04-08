from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('artists', views.artists, name='artists'),
    path('artists/<int:pk>/', views.show_artist, name="artist-details"),
    path('add_artist', views.add_artist, name='add-artist'),
    path('delete_artist/<int:pk>/', views.delete_artist, name='delete-artist'),
    path('update_artist/<int:pk>/', views.update_artist, name='update-artist'),
    path('albums', views.albums, name='albums'),
    path('add_album', views.add_album, name="add-album"),
    path('playlists', views.playlists, name='playlists'),
]
