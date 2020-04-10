from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import Podcast, Episode


class BlogEpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        exclude = ('file', 'image', 'active')


class BlogPodcastSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
