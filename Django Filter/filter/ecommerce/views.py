from django.shortcuts import render
from .models import Product
from .filters import ProductFilter

def product_list(request):
    products = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products)
    return render(request, 'ecommerce/product_list.html', {'filter': product_filter})


