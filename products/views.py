from django.shortcuts import render
from .models import Product
from .filters import ProductFilter


# display and filter products list based on model attributes
def product_list(request):
    product_list = Product.objects.all()
    f = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'products/product_list.html', {'filter': f})

