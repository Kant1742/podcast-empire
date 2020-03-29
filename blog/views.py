from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    View, DetailView, ListView, CreateView
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
    # paginate_by = 2


# Not the worst decision.
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
    model = Episode
    context_object_name = 'episode'

    def get(self, request, episode_slug, podcast_slug):
        # Reverse relationships. The lovercase name of the model inside the parentheses.
        # Podcast.objects.filter(episode__status__contains='Published')
        episode = Episode.objects.select_related('podcast').get(slug=episode_slug)
        # Total: 759.04ms. 2-7.00 ms (16 queries)
        podcast = get_object_or_404(Podcast, slug=podcast_slug)
        return render(request,
                      'blog/episode_detail.html',
                      {'episode': episode,
                      'podcast': podcast})
