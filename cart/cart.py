from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_SLUG)
        if not cart:
            # Save in a session the empty cart
            cart = self.session[settings.CART_SESSION_SLUG] = {}
        self.cart = cart

    def __iter__(self):
        product_slugs = self.cart.keys()
        # Receive objects of model 'Product' and send them in the cart.
        products = Product.objects.filter(slug__in=product_slugs)

        cart = self.cart.copy()
        for product in products:
            cart[product.slug]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Return total quantity of objects in a cart"""
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """Add a product in the cart or update its quantity"""
        product_slug = product.slug
        if product_slug not in self.cart:
            self.cart[product_slug] = {'quantity': 0,
                                       'price': str(product.price)}
        if update_quantity:
            self.cart[product_slug]['quantity'] = quantity
        else:
            self.cart[product_slug]['quantity'] += quantity
        self.save()

    def save(self):
        # Mark a session as updated
        self.session.modified = True

    def remove(self, product):
        """Remove a product from the cart"""
        product_slug = product.slug
        if product_slug in self.cart:
            del self.cart[product_slug]
            self.save()

    def get_total_price(self):
        return sum(
            Decimal(
                item['price']) * item['quantity']
                for item in self.cart.values()
        )

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_SLUG]
        self.save()
