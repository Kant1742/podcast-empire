from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    View, DetailView, ListView, CreateView
)
from django.views.generic.list import MultipleObjectMixin
from django.contrib import messages

from .models import Episode, Podcast
from .forms import PodcastCreateForm


class PodcastListView(ListView):
    model = Podcast
    context_object_name = 'podcasts'


class PodcastEpisodesDetailView(DetailView, MultipleObjectMixin):
    model = Podcast
    template_name = 'blog/podcast_episodes.html'
    object_list = Episode.objects.filter()
    paginate_by = 2

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['category'] = Podcast.objects.all()
    #     return context


class EpisodeListView(ListView):
    queryset = Episode.published.all()
    ordering = ['-publish']
    paginate_by = 2



class EpisodeDetailView(DetailView):
    model = Episode
    context_object_name = 'episode'

    # Shitty way, but here we are. Receiving 2 slugs in the urls and
    # in the template doesn't work in the way I tried
    def get(self, request, episode_slug, podcast_slug):
        episode = get_object_or_404(Episode, slug=episode_slug)
        podcast = get_object_or_404(Podcast, slug=podcast_slug)
        return render(request,
                      'blog/episode_detail.html',
                      {'episode': episode,
                       'podcast': podcast})
