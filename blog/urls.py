from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('',
         views.PodcastListView.as_view(),
         name='podcast_list'),
    path('episodes/',
         views.EpisodeListView.as_view(),
         name='episode_list'),
    path('<slug:slug>/',
         views.PodcastEpisodesDetailView.as_view(),
         name='podcast_detail'),
    path('<slug:podcast_slug>/episodes/<slug:episode_slug>/',
         views.EpisodeDetailView.as_view(),
         name='episode_detail'),
]
