from django.contrib import admin
from django.urls import path, include
from django_filters.views import FilterView
from products import views as product_views
from products.filters import ProductFilter


urlpatterns = [
    path('admin/', admin.site.urls),
    # use one of the following options 
    # path('products/', product_views.product_list, name='products'),
    path('products/', FilterView.as_view(
        filterset_class=ProductFilter, template_name='products/product_list.html'), name='products'),
]


