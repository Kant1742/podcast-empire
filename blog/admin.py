from django.contrib import admin
from .models import Episode, Podcast
# Register your models here.


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'podcast')
    list_filter = ('podcast',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'

    # TODO. Doesn't work
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100">')


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    list_filter = ('title',)
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}

    # Doesn't work
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100">')


admin.site.site_title = "Podcast Empire"
admin.site.site_header = 'Podcasts'

