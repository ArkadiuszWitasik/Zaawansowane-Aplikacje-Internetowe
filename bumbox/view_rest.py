from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import Artist, Album, Track, Playlist, Profile
from .serializers import ArtistSerializer, AlbumSerializer, AlbumGetSerializer, TrackSerializer, TrackGetSerializer, PlaylistSerializer, PlaylistGetSerializer, ProfileSerializer, UserSerializer

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def artists(request):
  if request.method == "GET":
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
  elif request.method == "POST":
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def artist(request, pk):
  try:
    artist = Artist.objects.get(pk=pk)
  except artist.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND) 

  if request.method == "GET":
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)
  elif request.method == "PUT":
    serializer = ArtistSerializer(artist, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    artist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def albums(request):
  if request.method == "GET":
    albums = Album.objects.all()
    serializer = AlbumGetSerializer(albums, many=True)
    return Response(serializer.data)
  elif request.method == "POST":
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def album(request, pk):
  try:
    album = Album.objects.get(pk=pk)
  except album.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND) 

  if request.method == "GET":
    serializer = AlbumGetSerializer(album)
    return Response(serializer.data)
  elif request.method == "PUT":
    serializer = AlbumSerializer(album, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    album.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def tracks(request):
  if request.method == "GET":
    tracks = Track.objects.all()
    serializer = TrackGetSerializer(tracks, many=True)
    return Response(serializer.data)
  elif request.method == "POST":
    serializer = TrackSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def track(request, pk):
  try:
    track = Track.objects.get(pk=pk)
  except track.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND) 

  if request.method == "GET":
    serializer = TrackGetSerializer(track)
    return Response(serializer.data)
  elif request.method == "PUT":
    serializer = TrackSerializer(track, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    track.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def playlists(request):
  if request.method == "GET":
    playlists = Playlist.objects.all()
    serializer = PlaylistGetSerializer(playlists, many=True)
    return Response(serializer.data)
  elif request.method == "POST":
    serializer = PlaylistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def playlist(request, pk):
  try:
    playlist = Playlist.objects.get(pk=pk)
  except playlist.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND) 

  if request.method == "GET":
    serializer = PlaylistGetSerializer(playlist)
    return Response(serializer.data)
  elif request.method == "PUT":
    serializer = PlaylistSerializer(playlist, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    playlist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if not hasattr(user, 'profile'):
                profile_data = {
                    'user': user,
                    'bio': request.data.get('bio', ''),
                    'favourite_genre': request.data.get('favourite_genre', ''),
                }
                Profile.objects.create(**profile_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)