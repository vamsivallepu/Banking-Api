from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    # GraphQL endpoint for making queries
    path("gql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]