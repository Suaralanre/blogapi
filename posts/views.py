from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


# Using viewsets for the related views

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = UserSerializer
