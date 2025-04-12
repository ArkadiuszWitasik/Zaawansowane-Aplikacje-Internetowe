import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
from django import forms
from .models import Artist, Album, Track, Playlist

class ArtistType(DjangoObjectType):
  class Meta:
    model = Artist
    fields = "__all__"

class AlbumType(DjangoObjectType):
  class Meta:
    model = Album
    fields = "__all__"

class TrackType(DjangoObjectType):
  class Meta:
    model = Track
    fields = "__all__"

class PlaylistType(DjangoObjectType):
  class Meta:
    model = Playlist
    fields = "__all__"

class ArtistForm(forms.ModelForm):
  class Meta:
    model = Artist
    fields = ['name', 'description', 'picture']

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = ['title', 'artist', 'genre', 'picture']

class TrackForm(forms.ModelForm):
  class Meta:
    model = Track
    fields = ['title', 'album', 'duration']

class PlaylistForm(forms.ModelForm):
  class Meta:
    model = Playlist
    fields = ['name', 'profile', 'tracks']

class CreateArtist(DjangoModelFormMutation):
  class Meta:
    form_class = ArtistForm

class CreateAlbum(DjangoModelFormMutation):
  class Meta:
    form_class = AlbumForm

class CreateTrack(DjangoModelFormMutation):
  class Meta:
    form_class = TrackForm

class CreatePlaylist(DjangoModelFormMutation):
  class Meta:
    form_class = PlaylistForm

class Query(graphene.ObjectType):
  all_artists = graphene.List(ArtistType)
  artist = graphene.Field(ArtistType, id=graphene.Int(required=True))
  all_albums = graphene.List(AlbumType)
  album = graphene.Field(AlbumType, id=graphene.Int(required=True))
  all_tracks = graphene.List(TrackType)
  track = graphene.Field(TrackType, id=graphene.Int(required=True))
  all_playlists = graphene.List(PlaylistType)
  playlist = graphene.Field(PlaylistType, id=graphene.Int(required=True))

  def resolve_all_artists(self, info):
    return Artist.objects.all()
  
  def resolve_artist(self, info, id):
    return Artist.objects.get(id=id)

  def resolve_all_albums(self, info):
    return Album.objects.all()

  def resolve_album(self, info, id):
    return Album.objects.get(id=id)

  def resolve_all_tracks(self, info):
      return Track.objects.all()

  def resolve_track(self, info, id):
    return Track.objects.get(id=id)

  def resolve_all_playlists(self, info):
      return Playlist.objects.all()

  def resolve_playlist(self, info, id):
    return Playlist.objects.get(id=id)

class Mutation(graphene.ObjectType):
  create_artist = CreateArtist.Field()
  create_album = CreateAlbum.Field()
  create_track = CreateTrack.Field()
  create_playlist = CreatePlaylist.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)