from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

# class CartAdd():
#     model = Cart
#     form = CartAddProductForm()

#     def get_context_data(self, product_slug, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product'] = get_object_or_404(Product, slug=product_slug)
#         return context

#     def form_valid(self, form):
#         cd = form.cleaned_data


def cart_remove(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    cart.remove(product)
    if cart:
        return redirect('cart:cart_detail')
    else:
        return redirect('shop/')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True}
        )
    return render(request, 'cart/detail.html', {'cart': cart})
