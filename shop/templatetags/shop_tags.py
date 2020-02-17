from django import template
from shop.models import Category, Product, ProductImage


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('shop/tags/last_products.html')
def get_last_products(count=7):
    products = ProductImage.objects.filter(is_active=True, is_main=True)
    ordered_products = products.order_by('id')[:count]
    return {'last_products': ordered_products}
