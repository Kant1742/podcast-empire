from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import Podcast, Episode
from taggit_serializer.serializers import (
    TagListSerializerField,
    TaggitSerializer
)


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class BlogEpisodeSerializer(serializers.ModelSerializer, TaggitSerializer):
    podcast = StringSerializer(many=False)
    tags = TagListSerializerField()

    class Meta:
        model = Episode
        exclude = ('file', 'image', 'active')


class BlogPodcastSerializer(serializers.ModelSerializer):
    podcast_episodes = BlogEpisodeSerializer(many=True)

    class Meta:
        model = Podcast
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
