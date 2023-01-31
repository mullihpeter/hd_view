from graphene_django import DjangoObjectType
from .models import Profile, CustomUser


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("user", "nickname", "uuid", "profile_pic", "age_limit")


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'
