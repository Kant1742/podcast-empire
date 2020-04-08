from rest_framework import serializers
from blog.models import Podcast, Episode


class BlogPodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'


class BlogEpisodeSerializer(serializers.ModelSerializer):
    podcast = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    
    class Meta:
        model = Episode
        exclude = ('file', 'image', 'active')
