from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import ProductListView, product_detail


class TestUrls(SimpleTestCase):

    def test_list_url_resolve(self):
        url = reverse('shop:product_list')
        self.assertEquals(resolve(url).func.view_class, ProductListView)

    def test_detail_url_resolve(self):
        url = reverse('shop:product_detail', args=['some_slug'])
        self.assertEquals(resolve(url).func, product_detail)
