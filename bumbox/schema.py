import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
from django import forms
from datetime import timedelta
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
  duration = graphene.Float()
  def resolve_duration(self, info):
    return self.duration.total_seconds() if self.duration else None

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

class UpdateArtist(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    name = graphene.String()
    description = graphene.String()

  artist = graphene.Field(lambda: ArtistType)

  def mutate(self, info, id, name=None, description=None):
    artist = Artist.objects.get(pk=id)
    if name:
      artist.name = name
    if description:
      artist.description = description
    artist.save()
    return UpdateArtist(artist=artist)

class UpdateAlbum(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    title = graphene.String()
    genre = graphene.String()
    artist_id = graphene.ID()
  
  album = graphene.Field(lambda: AlbumType)

  def mutate(self, info, id, title=None, genre=None, artist_id=None):
    album = Album.objects.get(pk=id)
    if title:
      album.title = title
    if genre:
      album.genre = genre
    if artist_id:
      artist = Artist.objects.get(pk=artist_id)
      album.artist = artist
    album.save()
    return UpdateAlbum(album=album)

class UpdateTrack(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    title = graphene.String()
    duration = graphene.String()
  track = graphene.Field(lambda: TrackType)

  def mutate(self, info, id, title=None, duration=None):
    track = Track.objects.get(pk=id)
    if title:
      track.title = title
    if duration:
      h, m, s = map(int, duration.split(':'))
      track.duration = timedelta(hours=h, minutes=m, seconds=s)
    track.save()
    return UpdateTrack(track=track)

class UpdatePlaylist(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    name = graphene.String()
    profile = graphene.ID()
    tracks = graphene.List(graphene.ID)
  playlist = graphene.Field(lambda: PlaylistType)
  
  def mutate(self, info, id, name=None, tracks=None):
    playlist = Playlist.objects.get(pk=id)
    updated_tracks = []
    if name:
      playlist.name = name
    if tracks:
      for track in tracks:
        try:
          track = Track.objects.get(pk=track)
          updated_tracks.append(track)
        except Track.DoesNotExist:
          continue
      playlist.tracks.set(updated_tracks)
    playlist.save()
    return UpdatePlaylist(playlist=playlist)

class DeleteArtist(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
  success = graphene.Boolean()
  def mutate(self, info, id):
    try:
      artist = Artist.objects.get(pk=id)
      artist.delete()
      return DeleteArtist(success=True)
    except Artist.DoesNotExist:
      return DeleteArtist(success=False)

class DeleteAlbum(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
  success = graphene.Boolean()
  def mutate(self, info, id):
    try:
      album = Album.objects.get(pk=id)
      album.delete()
      return DeleteAlbum(success=True)
    except:
      return DeleteAlbum(success=False)
    
class DeleteTrack(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
  success = graphene.Boolean()
  def mutate(self, info, id):
    try:
      track = Track.objects.get(pk=id)
      track.delete()
      return DeleteTrack(success=True)
    except:
      return DeleteTrack(success=False)
    
class DeletePlaylist(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
  success = graphene.Boolean()
  def mutate(self, info, id):
    try:
      playlist = Playlist.objects.get(pk=id)
      playlist.delete()
      return DeletePlaylist(success=True)
    except Playlist.DoesNotExist:
      return DeletePlaylist(success=False)
    
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
  update_artist = UpdateArtist.Field()
  update_album = UpdateAlbum.Field()
  update_track = UpdateTrack.Field()
  update_playlist = UpdatePlaylist.Field()
  delete_artist = DeleteArtist.Field()
  delete_album = DeleteAlbum.Field()
  delete_track = DeleteTrack.Field()
  delete_playlist = DeletePlaylist.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)