from django.test import TestCase
import datetime
from .models import Episode, Podcast


class PodcastModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Podcast.objects.create(
            id=100,
            title="test podcast title",
            slug="test-podcast-slug",
            description="test podcast descr",
            author="Be better",
            image='default_user.jpg',
            prefix_url="https=//chtbl.com/track/74377E/",
            category="Art",
            rss="http=//rss.castbox.fm/everest/f9a795b920d943dc8\
                12f0d3ee41095e4.xml"
        )

    def test_title_content(self):
        podcast = Podcast.objects.get(id=100)
        expected_object_name = f'{podcast.title}'
        self.assertEquals(expected_object_name, 'test podcast title')
    
    def test_description_content(self):
        podcast = Podcast.objects.get(id=100)
        expected_object_name = f'{podcast.description}'
        self.assertEquals(expected_object_name, 'test podcast descr')

