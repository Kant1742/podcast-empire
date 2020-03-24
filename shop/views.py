from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from cart.forms import CartAddProductForm
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    form = CartAddProductForm()

    # paginate_by = 10

    # A simple expample of get_context_data.
    # In template use {{ page_title }} and it returns text 'Author'
    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['page_title'] = 'Authors'
    #     return data



def product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug,
                                is_active=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product_detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
