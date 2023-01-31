from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from accounts.schema import schema as user_schema
from accounts.views import ProfileGraphQLView

urlpatterns = [
    path("users", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=user_schema))),
    path('profile/', ProfileGraphQLView.as_view(graphiql=True, schema=user_schema)),
]
