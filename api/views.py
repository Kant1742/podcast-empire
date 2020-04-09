from django.shortcuts import render

from rest_framework import generics, permissions

from blog.models import Episode, Podcast
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogEpisodeSerializer, BlogPodcastSerializer


class BlogPodcastListAPIView(generics.ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = BlogPodcastSerializer


class BlogPodcastDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = BlogPodcastSerializer
    # lookup_field = 'slug'


class BlogEpisodeListAPIView(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = BlogEpisodeSerializer


class BlogEpisodeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Episode.objects.all()
    serializer_class = BlogEpisodeSerializer
