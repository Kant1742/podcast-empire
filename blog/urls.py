from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = 'blog'


urlpatterns = [
     path('',
          cache_page(60*30)
          (views.PodcastListView.as_view()),
          name='podcast_list'),
     path('episodes/',
          views.EpisodeListView.as_view(),
          name='episode_list'),
     path('<slug:slug>/',
          cache_page(60*30)
          (views.PodcastEpisodesDetailView.as_view()),
          name='podcast_detail'),
     path('<slug:podcast_slug>/episodes/<slug:episode_slug>/',
          cache_page(60*30)
          (views.EpisodeDetailView.as_view()),
          name='episode_detail'),
]
