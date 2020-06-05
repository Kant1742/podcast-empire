from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ValidationError

# from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager
from PIL import Image

# The other way is using FileExtensionValidator


def validate_file_extension(value):
    accepted_values = ('.mp3', 'wav', '.aac', '.wma', '.flac', '.alac')
    if not value.name.endswith(accepted_values):
        raise ValidationError(f'Supported formats: {accepted_values}.')


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

    # ThumbnailerImageField(resize_source={ 'size': (300, 300), 'crop': 'scale' })
    # And then use <img src="{{ img.img.url }}"> in a themplate
    image = models.ImageField(
        upload_to='podcast-images', null=True, blank=True
    )

    author = models.CharField(max_length=100)
    prefix_url = models.CharField(max_length=40, blank=True)
    category = models.CharField(max_length=30,
                                choices=STATUS_CHOICES,
                                default='music')
    # subscribers = models.IntegerField(blank=True, null=True) # TODO ManyToManyField and another class?
    downloads = models.IntegerField(blank=True, null=True) # TODO count total downloads from all episodes
    rss = models.URLField(blank=True) # parser

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
    podcast = models.ForeignKey(Podcast,
                                on_delete=models.CASCADE,
                                related_name='podcast_episodes')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(blank=True,
                              null=True,
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
    downloads = models.IntegerField(blank=True, null=True) # TODO again count downloads/plays
    file = models.FileField(upload_to='files',
                            validators=[validate_file_extension]
                            )
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
