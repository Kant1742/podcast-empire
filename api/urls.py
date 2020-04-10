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
