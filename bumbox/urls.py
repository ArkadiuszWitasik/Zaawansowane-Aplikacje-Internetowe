from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import view_rest
from . import views

resturlpatterns = [
  path('api/create_user', view_rest.create_user),
  path('api/album/', view_rest.albums),
  path('api/album/<int:pk>', view_rest.album),
  path('api/artist/', view_rest.artists),
  path('api/artist/<int:pk>', view_rest.artist),
  path('api/track/', view_rest.tracks),
  path('api/track/<int:pk>', view_rest.track),
  path('api/playlist/', view_rest.playlists),
  path('api/playlist/<int:pk>', view_rest.playlist),
  path('api/token', TokenObtainPairView.as_view()),
  path('api/token/refresh/', TokenRefreshView.as_view()),
  path('api/token/verify/', TokenVerifyView.as_view()),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user', views.login_user, name='login-user'),
    path('logout_user', views.logout_user, name='logout-user'),
    path('register_user', views.register_user, name='register-user'),
    path('artists', views.artists, name='artists'),
    path('artists/<int:pk>/', views.show_artist, name="artist-details"),
    path('add_artist', views.add_artist, name='add-artist'),
    path('delete_artist/<int:pk>/', views.delete_artist, name='delete-artist'),
    path('update_artist/<int:pk>/', views.update_artist, name='update-artist'),
    path('albums', views.albums, name='albums'),
    path('albums/<int:pk>/', views.show_album, name="album-details"),
    path('add_album', views.add_album, name="add-album"),
    path('delete_album/<int:pk>/', views.delete_album, name='delete-album'),
    path('update_album/<int:pk>/', views.update_album, name='update-album'),
    path('albums/<int:pk>/add_track', views.add_track, name="add-track"),
    path('albums/<int:pk>/update_track/<int:pk2>/', views.update_track, name="update-track"),
    path('albums/<int:pk>/delete_track/<int:pk2>/', views.delete_track, name="delete-track"),
    path('playlists', views.playlists, name='playlists'),
    path('add_playlist', views.add_playlist, name='add-playlist'),
    path('update_playlist/<int:pk>/', views.update_playlist, name="update-playlist"),
    path('delete_playlist/<int:pk>/', views.delete_playlist, name="delete-playlist"),
] + resturlpatterns
