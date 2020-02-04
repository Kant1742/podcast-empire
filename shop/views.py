from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
