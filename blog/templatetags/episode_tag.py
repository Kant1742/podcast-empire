from django import template
from blog.models import Episode

register = template.Library()


@register.inclusion_tag('blog/tags/last_episodes.html')
def get_last_episodes(count=5):
    episodes = Episode.objects.order_by('id')[:count]
    return {'last_episodes': episodes}
