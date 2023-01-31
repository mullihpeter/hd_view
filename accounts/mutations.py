import graphene
import graphql_jwt
from graphql_auth import mutations
from graphql_jwt.decorators import login_required
from accounts.models import CustomUser, Profile
from accounts.types import CustomUserType, ProfileType


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, username, password):
        user = CustomUser(username=username)
        user.set_password(password)
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
        if user != user:
            raise Exception("You're not allowed to edit this data!!")
        user.username = username
        user.email = email
        user.save()
        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):
    class Arguments:
        uuid = graphene.ID()
        # email = graphene.String(required=False)
        # username = graphene.String(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    @login_required
    def mutate(cls, root, info, uuid):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not Logged in! Please login now")
        user = CustomUser.objects.get(uuid=uuid)
        user.delete()
        return

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

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    # django-graphql-jwt inheritances

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
