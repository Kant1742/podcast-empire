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


# class PodcastEpisodesDetailView(DetailView, MultipleObjectMixin):
#     model = Podcast
#     template_name = 'blog/podcast_episodes.html'
#     object_list = Episode.published.all()
#     # Fuck. Doesn't work properly with pagination
#     paginate_by = 5

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['object_list'] = Episode.objects.filter(
#             podcast__slug__exact=self.kwargs['slug']
#         )
#         return context


class PodcastEpisodesDetailView(DetailView):
    model = Podcast
    template_name = 'blog/podcast_episodes.html'
    # paginate_by = 2


# Not the worst decision.
# class PodcastEpisodesDetailView(ListView):
#     model = Episode
#     template_name = 'blog/podcast_episodes.html'
#     paginate_by = 5

#     def get_queryset(self):
#         return self.model.objects.all().filter(
#             podcast__slug__exact=self.kwargs['slug']).order_by('-publish')


# Fuck
# class PodcastEpisodesDetailView(ListView):
#     template_name = 'blog/podcast_episodes.html'
#     paginate_by = 2

#     def get_queryset(self, *args, **kwargs):
#         podcast = Podcast.objects.filter(podcast_episodes__slug=self.request.GET.get('slug'))
#         queryset = super(PodcastEpisodesDetailView, self).get_queryset(*args, **kwargs)
#         return queryset


class EpisodeListView(ListView):
    queryset = Episode.published.all() #.only('podcast', 'title', 'image', 'description')
    ordering = ['-publish']
    paginate_by = 10


class EpisodeDetailView(DetailView):
    model = Episode
    context_object_name = 'episode'

    # Another shitty way, but here we are. Receiving 2 slugs in
    # the urls and in the template doesn't work in the way I tried
    def get(self, request, episode_slug, podcast_slug):
        episode = get_object_or_404(Episode, slug=episode_slug)
        podcast = get_object_or_404(Podcast, slug=podcast_slug)
        return render(request,
                      'blog/episode_detail.html',
                      {'episode': episode,
                       'podcast': podcast})
