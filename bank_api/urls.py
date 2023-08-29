from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # GraphQL endpoint for making queries
    path("gql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
