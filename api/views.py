from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, viewsets

from blog.models import Episode, Podcast
from .permissions import IsOwnerOrReadOnly
from .serializers import (BlogEpisodeSerializer,
                          BlogPodcastSerializer,
                          UserSerializer)


class BlogPodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = BlogPodcastSerializer


# class BlogPodcastDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Podcast.objects.all()
#     serializer_class = BlogPodcastSerializer
#     # lookup_field = 'slug'


class BlogEpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = BlogEpisodeSerializer


# class BlogEpisodeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (IsOwnerOrReadOnly,)
#     queryset = Episode.objects.all()
#     serializer_class = BlogEpisodeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
