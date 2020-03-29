from django import template
from blog.models import Episode
from PIL import Image

register = template.Library()

@register.inclusion_tag('blog/tags/last_episodes.html')
def get_last_episodes(count=5):
    episodes = Episode.objects.order_by('id')[:count].only('title')

    # img = Image.open(image.path)

    # if img.height > 300 and img.width > 300:
    #     output_size = (300, 300)
    #     img.thumbnail(output_size)
    #     img.save(image.path)

    return {'last_episodes': episodes}
