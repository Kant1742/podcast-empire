from django.db import models
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Podcast(models.Model):
    STATUS_CHOICES = (
        ('music', 'Music'),
        ('art', 'Art') # And so on...
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='podcast-images')
    author = models.CharField(max_length=100)
    prefix_url = models.CharField(max_length=40, blank=True)
    category = models.CharField(max_length=30,
                                choices=STATUS_CHOICES,
                                default='music')
    # subscribers = models.IntegerField(blank=True, null=True)
    # downloads = models.IntegerField(blank=True, null=True)
    rss = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:podcast_detail',
                       kwargs={'slug': self.slug})

 
class Episode(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # To this podcast we have to refer in a opposite way.
    # podcast.episode_set.all for example (?)
    podcast = models.ForeignKey(Podcast,
                                on_delete=models.CASCADE,
                                related_name='podcast_episodes')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(blank=True, upload_to='episode-images')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    # Create schedule for posting
    # Or make default publish time at 2:31 pm UTC+3
    publish = models.DateTimeField(default=timezone.now)
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # New manager
    # downloads = models.IntegerField(blank=True, mull=True)
    file = models.FileField(upload_to='files')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self, podcast):
        return reverse('blog:episode_detail',
                       kwargs={'slug': self.slug})
