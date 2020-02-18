from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import (
    Category, Product, ProductImage)


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(ProductImage)
class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


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
    list_display = ('name', 'description', 'category', 'price', 'is_active', 'created', 'updated')
    list_display_links= ('name',)
    list_filter= ('category', 'is_active', 'created', 'updated')
    list_editable= ('price', 'is_active')
    search_fields= ('name',)
    prepopulated_fields= {'slug': ('name',)}
    inlines= [ProductImageInline]
    readonly_fields= ('get_image',)
    form= ProductAdminForm

    def get_image(self, obj):
        obj= ProductImage.objects.filter(is_main=True)
        return mark_safe(
            f'<img src={obj.image.url} width="100" height="100">'
        )

    get_image.short_description = "Product Image"


# admin.site.register(ProductInOrder)
# admin.site.register(Order)
# admin.site.register(Status)
