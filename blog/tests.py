import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Episode, Podcast


class PodcastModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(
            username='test_user1', password='qwe123')
        test_user1.save()

        Podcast.objects.create(
            id=100,
            title="test podcast title",
            slug="test-podcast-slug",
            description="test podcast descr",
            author=test_user1,
            image='default_user.jpg',
            prefix_url="https=//chtbl.com/track/74377E/",
            category="Art",
            rss="http=//rss.castbox.fm/everest/f9a795b920d943dc8\
                12f0d3ee41095e4.xml"
        )

    def test_podcast_content(self):
        podcast = Podcast.objects.get(id=100)
        author = f'{podcast.author}'
        title = f'{podcast.title}'
        description = f'{podcast.description}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'test podcast title')
        self.assertEqual(description, 'test podcast descr')

