from django.contrib.auth import get_user_model
from rest_framework.serializers import ReadOnlyField
from dj_rest_auth.serializers import UserDetailsSerializer

from .models import Post


class PostSerializer(UserDetailsSerializer):

    username = ReadOnlyField(source="author.username")

    class Meta(UserDetailsSerializer.Meta):
        fields = (
            "id",
            "username",
            "title",
            "body",
            "created_at",
        )
        model = Post


class UserSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        model = get_user_model()
        fields = ("id", "username")
