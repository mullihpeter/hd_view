import graphene
from .mutations import CreateUser, UpdateUser, DeleteUser, AuthMutation
from .types import CustomUserType, ProfileType
from .models import Profile, CustomUser
from graphql_auth.schema import UserQuery, MeQuery


class Query(UserQuery, MeQuery, graphene.ObjectType):
    profile_data = graphene.List(ProfileType)
    user_data = graphene.List(CustomUserType)

    def resolve_user_data(root, info):
        return CustomUser.objects.all()

    def resolve_profile_data(root, info):
        return Profile.objects.all()


class Mutation(AuthMutation, graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
