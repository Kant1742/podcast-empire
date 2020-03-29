from django.utils.deprecation import MiddlewareMixin
from .models import Episode

class LastEpisodes(MiddlewareMixin):
    def process_request(self, request, count=5):
        episodes = Episode.objects.order_by('id')[:count].only('image', 'title')
        request.episodes = episodes
        return None
