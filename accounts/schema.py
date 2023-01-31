import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from .models import Profile, CustomUser
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
from graphql_jwt.decorators import login_required, superuser_required


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field()  # For passwordless registration
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("user", "nickname", "uuid", "profile_pic", "age_limit")


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class Query(UserQuery, MeQuery, graphene.ObjectType):
    profile_data = graphene.List(ProfileType)
    user_data = graphene.List(CustomUserType)

    def resolve_user_data(root, info):
        return CustomUser.objects.all()

    def resolve_profile_data(root, info):
        return Profile.objects.all()


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    @superuser_required
    def mutate(cls, root, info, username):
        user = CustomUser(username=username)
        user.save()
        return CreateUser(user=user)


# updating user mutation
class UpdateUser(graphene.Mutation):
    class Arguments:
        uuid = graphene.ID()
        email = graphene.String(required=False)
        username = graphene.String(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    @login_required
    def mutate(cls, root, info, username, uuid, email):
        user = CustomUser.objects.get(uuid=uuid)
        user.username = username
        user.email = email
        user.save()
        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):
    class Arguments:
        uuid = graphene.ID()
        #email = graphene.String(required=False)
        #username = graphene.String(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    @login_required
    def mutate(cls, root, info, uuid):
        user = CustomUser.objects.get(uuid=uuid)
        user.delete()
        return


class Mutation(AuthMutation, graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
