import graphene
import bumbox.schema

class Query(bumbox.schema.Query, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)