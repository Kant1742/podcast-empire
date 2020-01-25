from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    View, DetailView, ListView, CreateView
)
from django.contrib import messages
from .models import Episode, Podcast
from .forms import PodcastCreateForm


class PodcastListView(ListView):
    model = Podcast
    context_object_name = 'podcasts'


class PodcastDetailView(DetailView):
    model = Podcast


class PodcastCreateView(CreateView):
    model = Podcast
    fields = '__all__'
    template_name = 'blog/podcast_create.html'
    # By default template_name = podcast_form.html

    def post(self, request):
        if request.method == 'POST':
            form = PodcastCreateForm(request.POST)
        if form.is_valid():
            form.save()
            podcast = form.cleaned_data.get('podcast')
            messages.success(
                request,
                f'The podcast {self.object}has been successfully created'
            )
            return redirect('/')
        else:
            form = PodcastCreateForm()
        return render(request, 'blog/podcast_create.html', {'form': form})





class EpisodeListView(ListView):
    queryset = Episode.published.all()
    context_object_name = 'episodes'


class EpisodeDetailView(DetailView):
    model = Episode
    context_object_name = 'episode'
    slug_field = 'slug'
