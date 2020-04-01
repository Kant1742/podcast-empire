from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView,
    ListView,
)
from django.views.generic.list import MultipleObjectMixin
from django.contrib import messages

from .models import Episode, Podcast
from .forms import PodcastCreateForm


# Tried to use Django Silk. Looks terrible.

class PodcastListView(ListView):
    model = Podcast
    context_object_name = 'podcasts'


class PodcastEpisodesDetailView(DetailView):
    model = Podcast
    template_name = 'blog/podcast_episodes.html'


class EpisodeListView(ListView):
    queryset = Episode.published.select_related('podcast') # .only('podcast',
                                                                # 'title',
                                                                # 'image',
                                                                # 'description')
    # .defer('title') is the opposite of .only()
    # It returns everything except of 'title'.
    ordering = ['-publish']
    paginate_by = 10


class EpisodeDetailView(DetailView):
    # model = Episode

    def get(self, request, episode_slug, podcast_slug):
        episode = get_object_or_404(Episode, slug=episode_slug, podcast__slug=podcast_slug)
        return render(request,
                      'blog/episode_detail.html',
                      {'episode': episode})
