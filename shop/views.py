from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from cart.forms import CartAddProductForm
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    # paginate_by = 10

    # A simple expample of get_context_data.
    # In template use {{ page_title }} and it returns text 'Author'
    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['page_title'] = 'Authors'
    #     return data

    # def get_context_data(self, *args, **kwargs):
    #     product_images = ProductImage.objects.all()
    #     products = Product.objects.filter(is_active=True)
    #     context = super().get_context_data(*args, **kwargs)
    #     context['prod_image'] = product_images.filter(is_main=True, product=get_object_or_404(ProductImage, product_images))
    #     return context

    # def get_context_data(self, *args, category_slug=None, **kwargs):
    #     category = None
    #     categories = Category.objects.all()
    #     products = Product.objects.filter(is_active=True)
    #     context = super().get_context_data(*args, **kwargs)
    #     if category_slug:
    #         context['category'] = get_object_or_404(
    #             Category, slug=category_slug)
    #         context['products'] = products.filter(category=context['category'])
    #     return context


# class ProductDetailView(DetailView):
#     model = Product
#     form = CartAddProductForm

def product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug,
                                is_active=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product_detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
