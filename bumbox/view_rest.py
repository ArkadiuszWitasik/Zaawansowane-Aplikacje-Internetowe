from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Artist, Album, Track, Playlist
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer, PlaylistSerializer

@api_view(['GET', 'POST'])
def arists(request):
  if request.method == "GET":
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return JsonResponse({'artists': serializer.data})
  if request.method == "POST":
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
  return JsonResponse({'message': 'message'})

@api_view(['GET', 'PUT', 'DELETE'])
def arist(request, pk):
  try:
    arist = arist.objects.get(pk=pk)
  except arist.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND) 

  if request.method == "GET":
    pass
  elif request.method == "PUT":
    pass
  elif request.method == "DELETE":
    pass

@api_view(['GET', 'POST'])
def albums(request):
  if request.method == "GET":
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return JsonResponse({'albums': serializer.data})
  if request.method == "POST":
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
  return JsonResponse({'message': 'message'})

@api_view(['GET', 'PUT', 'DELETE'])
def album(request, pk):
  try:
    album = album.objects.get(pk=pk)
  except album.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND) 

  if request.method == "GET":
    pass
  elif request.method == "PUT":
    pass
  elif request.method == "DELETE":
    pass

@api_view(['GET', 'POST'])
def tracks(request):
  if request.method == "GET":
    tracks = Track.objects.all()
    serializer = TrackSerializer(tracks, many=True)
    return JsonResponse({'tracks': serializer.data})
  if request.method == "POST":
    serializer = TrackSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
  return JsonResponse({'message': 'message'})

@api_view(['GET', 'PUT', 'DELETE'])
def track(request, pk):
  try:
    track = track.objects.get(pk=pk)
  except track.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND) 

  if request.method == "GET":
    pass
  elif request.method == "PUT":
    pass
  elif request.method == "DELETE":
    pass

@api_view(['GET', 'POST'])
def playlists(request):
  if request.method == "GET":
    playlists = Playlist.objects.all()
    serializer = PlaylistSerializer(playlists, many=True)
    return JsonResponse({'playlists': serializer.data})
  if request.method == "POST":
    serializer = PlaylistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
  return JsonResponse({'message': 'message'})

@api_view(['GET', 'PUT', 'DELETE'])
def playlist(request, pk):
  try:
    playlist = playlist.objects.get(pk=pk)
  except playlist.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND) 

  if request.method == "GET":
    pass
  elif request.method == "PUT":
    pass
  elif request.method == "DELETE":
    pass