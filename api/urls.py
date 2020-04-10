from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    BlogPodcastViewSet,
    BlogEpisodeViewSet,
    UserViewSet,
)

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('episodes', BlogEpisodeViewSet, basename='episodes')
router.register('', BlogPodcastViewSet, basename='podcasts')

urlpatterns = router.urls

# urlpatterns = [
#     path('users/', UserListAPIView.as_view()),
#     path('users/<int:pk>/', UserDetailAPIView.as_view()),
#     path('episodes/<int:pk>/', BlogEpisodeDetailAPIView.as_view()),
#     path('episodes/', BlogEpisodeListAPIView.as_view()),
#     path('', BlogPodcastListAPIView.as_view()),
#     path('<int:pk>/', BlogPodcastDetailAPIView.as_view()),
# ]
