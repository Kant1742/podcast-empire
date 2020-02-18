from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from PIL import Image


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(
        upload_to='category-images', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       kwargs={'slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    description = models.TextField()
    short_description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    # As the main image 
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True, default='no-image.jpg')
    # objects = models.Manager()  # Default manager
    # published = PublishedManager()  # New manager

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       kwargs={'slug': self.slug})


class ProductImage(models.Model):
    # Other images for a product
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True, default=None,
        related_name='product_image')
    image = models.ImageField(
        upload_to='product-images/%Y/%m/%d', default='no-image.jpg')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

"""
# Or use choices?
class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Status {self.name}'

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

class Order(models.Model):
    # total price for all products in order
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    customer_name = models.CharField(max_length=55)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(
        max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=120, null=True)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order № {self.id}, {self.status.name}'

    def save(self, *args, **kwargs):
        return super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    # Best way?
    price_per_item = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)  # price*quantity

    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product.name}'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        print(self.quantity)

        self.total_price = int(self.quantity) * price_per_item

        return super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(
        order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)
"""