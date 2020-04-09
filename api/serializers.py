from rest_framework import serializers
from blog.models import Podcast, Episode


class BlogEpisodeSerializer(serializers.ModelSerializer):
    # podcast = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Episode
        exclude = ('file', 'image', 'active')


class BlogPodcastSerializer(serializers.ModelSerializer):
    # podcast_episodes = BlogEpisodeSerializer(blank=True, many=True) # Redundant

    class Meta:
        model = Podcast
        fields = '__all__'
