from django.test import TestCase
from django.contrib.auth.models import User
from bumbox.models import Album,Artist,Playlist,Profile,Track
from datetime import timedelta

class ArtistModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name='Artist Name', description='A talented artist')

    def test_artist_str(self):
        self.assertEqual(str(self.artist), 'Artist Name')

    def test_artist_description(self):
        self.assertEqual(self.artist.description, 'A talented artist')


class AlbumModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name='Artist Name', description='Artist desc')
        self.album = Album.objects.create(title='Album Title', artist=self.artist, genre='ROCK')

    def test_album_str(self):
        self.assertEqual(str(self.album), 'Album Title')

    def test_album_artist_relation(self):
        self.assertEqual(self.album.artist.name, 'Artist Name')

    def test_album_genre(self):
        self.assertEqual(self.album.genre, 'ROCK')


class TrackModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name='Artist')
        self.album = Album.objects.create(title='Album', artist=self.artist, genre='POP')
        self.track = Track.objects.create(title='Track 1', album=self.album, duration=timedelta(minutes=3))

    def test_track_str(self):
        self.assertEqual(str(self.track), 'Track 1')

    def test_track_duration(self):
        self.assertEqual(self.track.duration, timedelta(minutes=3))

    def test_track_album_relation(self):
        self.assertEqual(self.track.album.title, 'Album')


class PlaylistModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user123', password='pass123')
        self.profile, _ = Profile.objects.get_or_create(user=self.user)

        self.artist = Artist.objects.create(name='Artist')
        self.album = Album.objects.create(title='Album', artist=self.artist, genre='POP')
        self.track1 = Track.objects.create(title='Track 1', album=self.album, duration=timedelta(minutes=2))
        self.track2 = Track.objects.create(title='Track 2', album=self.album, duration=timedelta(minutes=3))

        self.playlist = Playlist.objects.create(name='My Playlist', profile=self.profile)
        self.playlist.tracks.set([self.track1, self.track2])

    def test_playlist_str(self):
        self.assertEqual(str(self.playlist), 'My Playlist')

    def test_playlist_track_count(self):
        self.assertEqual(self.playlist.tracks.count(), 2)

    def test_playlist_contains_specific_track(self):
        self.assertIn(self.track1, self.playlist.tracks.all())