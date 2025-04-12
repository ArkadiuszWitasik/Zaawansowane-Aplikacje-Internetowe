from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from bumbox.models import Artist, Album, Track, Playlist, Profile
from django.contrib.auth.models import User
from datetime import timedelta

class ArtistViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.artist = Artist.objects.create(name='Artist 1', description='Description 1')
        self.admin_user = User.objects.create_user(username='admin', password='admin')
        self.client.login(username='admin', password='admin')

    def test_get_artists_list(self):
        response = self.client.get('/api/artist/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_artist(self):
        data = {'name': 'Artist 2', 'description': 'Description 2'}
        response = self.client.post('/api/artist/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Artist.objects.count(), 2)

    def test_get_single_artist(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(f'/api/artist/{self.artist.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Artist 1')

    def test_update_artist(self):
        self.client.force_authenticate(user=self.admin_user)
        data = {'name': 'Updated Artist 1'}
        response = self.client.put(f'/api/artist/{self.artist.id}', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.artist.refresh_from_db()
        self.assertEqual(self.artist.name, 'Updated Artist 1')

    def test_delete_artist(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(f'/api/artist/{self.artist.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artist.objects.count(), 0)

class AlbumViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin', password='admin')
        self.artist = Artist.objects.create(name='Artist 1', description='Description 1')
        self.album = Album.objects.create(title='Album 1', artist=self.artist, genre='POP')
        self.client.force_authenticate(user=self.user)

    def test_get_albums_list(self):
        response = self.client.get('/api/album/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_album(self):
        data = {
            'title': 'Album 2',
            'artist': self.artist.id,
            'genre': 'ROCK'
        }
        response = self.client.post('/api/album/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Album.objects.count(), 2)

    def test_get_album(self):
        response = self.client.get(f'/api/album/{self.album.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_album(self):
        data = {'title': 'Updated Title 1'}
        response = self.client.put(f'/api/album/{self.album.id}', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.album.refresh_from_db()
        self.assertEqual(self.album.title, 'Updated Title 1')

    def test_delete_album(self):
        response = self.client.delete(f'/api/album/{self.album.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Album.objects.count(), 0)


class TrackViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin', password='admin')
        self.artist = Artist.objects.create(name='Artist 1', description='Description 1')
        self.album = Album.objects.create(title='Album 1', artist=self.artist, genre='POP')
        self.track = Track.objects.create(title='Track 1', album=self.album, duration=timedelta(minutes=3))
        self.client.force_authenticate(user=self.user)

    def test_get_tracks_list(self):
        response = self.client.get('/api/track/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_track(self):
        data = {
            'title': 'Track 2',
            'album': self.album.id,
            'duration': '00:04:00'
        }
        response = self.client.post('/api/track/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Track.objects.count(), 2)

    def test_get_track(self):
        response = self.client.get(f'/api/track/{self.track.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_track(self):
        data = {'title': 'Updated Track 1'}
        response = self.client.put(f'/api/track/{self.track.id}', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.track.refresh_from_db()
        self.assertEqual(self.track.title, 'Updated Track 1')

    def test_delete_track(self):
        response = self.client.delete(f'/api/track/{self.track.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Track.objects.count(), 0)


class PlaylistViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin', password='admin')
        self.profile, _ = Profile.objects.get_or_create(user=self.user)
        self.artist = Artist.objects.create(name='Artist 1', description='Description 1')
        self.album = Album.objects.create(title='Album 1', artist=self.artist, genre='POP')
        self.track = Track.objects.create(title='Track 1' , album=self.album, duration=timedelta(minutes=3))
        self.playlist = Playlist.objects.create(name='Playlist 1', profile=self.profile)
        self.playlist.tracks.add(self.track)
        self.client.force_authenticate(user=self.user)

    def test_get_playlists_list(self):
        response = self.client.get('/api/playlist/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_playlist(self):
        data = {
            'name': 'Playlist 2',
            'profile': self.profile.id,
            'tracks': [self.track.id]
        }
        response = self.client.post('/api/playlist/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Playlist.objects.count(), 2)
        new_playlist = Playlist.objects.last()
        self.assertEqual(new_playlist.name, 'Playlist 2')
        self.assertEqual(new_playlist.profile, self.profile)
        self.assertEqual(new_playlist.tracks.count(), 1)
