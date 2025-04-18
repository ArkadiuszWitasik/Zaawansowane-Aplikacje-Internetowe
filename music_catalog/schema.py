import graphene
import graphql_jwt
import bumbox.schema

class Query(bumbox.schema.Query, graphene.ObjectType):
  pass

class Mutation(bumbox.schema.Mutation, graphene.ObjectType):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)