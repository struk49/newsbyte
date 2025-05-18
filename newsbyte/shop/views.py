from django.views.generic import ListView, DetailView
from .models import Product

class ShopListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
