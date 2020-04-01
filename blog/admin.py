from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Episode, Podcast

# In a template has to use filter 'safe' for a description
class EpisodeAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Episode
        fields = '__all__'


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'publish',
                    'status', 'get_podcast_image', 'podcast')
    list_filter = ('podcast', 'publish', 'status')
    list_display_links = ('title', 'get_image',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'podcast__title')
    date_hierarchy = 'publish'
    actions = ['make_unpublished', 'make_published']
    readonly_fields = ('get_image',)
    save_as = True
    save_on_top = True
    list_editable = ('status', 'publish')
    form = EpisodeAdminForm

    fieldsets = (
        ('Main', {
            "fields": ("podcast",)
        }),
        (None, {
            "fields": ("title", "description")
        }),
        ('Media', {
            "fields": ("image", "get_image", 'file')
        }),
        ("Options", {
            "fields": (('publish',), ('tags', "slug", "status", 'active',),)
        }),
    )

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} width="100" height="100"'
            )
        else:
            return mark_safe(
                f'<img src={obj.podcast.image.url} width="100" height="100"'
            )

    get_image.short_description = "Episode Image"

    def get_podcast_image(self, obj):
        return mark_safe(
            f'<img src={obj.podcast.image.url} width="100" height="100"'
        )

    get_podcast_image.short_description = "Podcast Image"

    def make_unpublished(self, request, queryset):
        """Unpublish an Episode"""
        row_update = queryset.update(status='draft')
        if row_update == 1:
            message_bit = "1 episode have been unpublished"
        else:
            message_bit = f"{row_update} episodes have been unpublished"
        self.message_user(request, f"{message_bit}")

    make_unpublished.allowed_permissions = ('change',)
    make_unpublished.short_description = ('Unpublish')

    def make_published(self, request, queryset):
        """Publish an Episode"""
        row_update = queryset.update(status='published')
        if row_update == 1:
            message_bit = "1 episode has been published"
        else:
            message_bit = f"{row_update} episodes have been published"
        self.message_user(request, f"{message_bit}")

    make_published.allowed_permissions = ('change', )
    make_published.short_description = ('Publish')


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 0
    readonly_fields = ('get_image',)

    fieldsets = (
        ('Main', {
            "fields": (("podcast",),)
        }),
        (None, {
            "fields": (("title", "description"),)
        }),
        (None, {
            "fields": ("publish",)
        }),
        ('Media', {
            "fields": ("get_image", "image", 'file')
        }),
        ("Options", {
            "fields": ("slug", "status", 'active')
        }),
    )

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} width="100" height="100"'
            )
        else:
            return mark_safe(
                f'<img src={obj.podcast.image.url} width="100" height="100"'
            )

    get_image.short_description = "Episode Image"


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'description', 'author', 'category')
    list_display_links = ('title', 'get_image',)
    list_filter = ('author', 'category')
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('get_image', )
    inlines = [EpisodeInline]
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width="100" height="100">'
        )

    get_image.short_description = "Podcast Image"

    fieldsets = (
        ('Main', {
            "fields": ("title", 'description', ("author", "category"))
        }),
        ('Image', {
            "fields": ("image", "get_image")
        }),
        ("Technical", {
            "fields": ("slug", "prefix_url", 'rss',)
        }),
    )


admin.site.site_title = "Podcast Empire"
admin.site.site_header = 'Podcasts'
