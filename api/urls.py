from django.urls import path

from .views import (
    BlogEpisodeListAPIView,
    BlogPodcastListAPIView,
    BlogEpisodeDetailAPIView,
    BlogPodcastDetailAPIView
)

urlpatterns = [
    path('', BlogPodcastListAPIView.as_view()),
    path('episodes/', BlogEpisodeListAPIView.as_view()),
    path('<slug:slug>/', BlogPodcastDetailAPIView.as_view()),
    path('episodes/<int:pk>/', BlogEpisodeDetailAPIView.as_view()),
]
