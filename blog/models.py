from django.db import models
from django.utils import timezone
from django.urls import reverse
# from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager
from PIL import Image


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Podcast(models.Model):
    STATUS_CHOICES = (
        ('Art', 'Art'),
        ('Business', 'Business'),
        ('Comedy', 'Comedy'),
        ('Education', 'Education'),
        ('Games & Hobbies', 'Games & Hobbies'),
        ('Government & Organizations', 'Government & Organizations'),
        ('Health', 'Health'),
        ('Kids & Family', 'Kids & Family'),
        ('Music', 'Music'),
        ('News & Politics', 'News & Politics'),
        ('Religion & Spirituality', 'Religion & Spirituality'),
        ('Science & Medicine', 'Science & Medicine'),
        ('Society & Culture', 'Society & Culture'),
        ('Sports & Recreation', 'Sports & Recreation'),
        ('Technology', 'Technology'),
        ('TV & Film', 'TV & Film'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='podcast-images', null=True, blank=True)
    # ThumbnailerImageField(resize_source={ 'size': (300, 300), 'crop': 'scale' })
    # And then use <img src="{{ img.img.url }}"> in a themplate
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

    # ThumbnailerImageField is another way
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Episode(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # To this podcast we have to refer in the opposite way.
    # We do it from a podcast
    # podcast.episode_set.all() by default or in other case related_name
    podcast = models.ForeignKey(Podcast,
                                on_delete=models.CASCADE,
                                related_name='podcast_episodes')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(blank=True,
                              upload_to='episode-images',
                              default='Django.jpg')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    # TODO Create schedule for posting
    # Or make default publish time at 2:31 pm UTC+3
    publish = models.DateTimeField(default=timezone.now)
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # New manager
    # downloads = models.IntegerField(blank=True, mull=True)
    file = models.FileField(upload_to='files')
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self, podcast):
        return reverse('blog:episode_detail',
                       kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
