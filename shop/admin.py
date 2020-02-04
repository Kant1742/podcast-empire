from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')
    list_display_links = ('name', 'get_image')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width="100" height="100">'
        )

    get_image.short_description = "Category Image"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'description', 'category')
    list_display_links = ('title', 'get_image',)
    list_filter = ('category',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width="100" height="100">'
        )

    get_image.short_description = "Product Image"
