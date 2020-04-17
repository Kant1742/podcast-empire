from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets, views

from blog.models import Episode, Podcast
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    BlogEpisodeSerializer,
    BlogPodcastSerializer,
    UserSerializer,
)


class BlogPodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = BlogPodcastSerializer


class BlogEpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = BlogEpisodeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
