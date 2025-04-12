import graphene
from graphene_django import DjangoObjectType
from .models import Artist

class ArtistType(DjangoObjectType):
  class Meta:
    model = Artist
    fields: "__all__"

class Query(graphene.ObjectType):
  all_artists = graphene.List(ArtistType)

  def resolve_all_artists(root, info):
    return Artist.objects.all()
  
schema = graphene.Schema(query=Query)