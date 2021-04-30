from django.contrib import admin
from django.urls import path, include
from products import views as product_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # in this url we'll display and filter products list 
    path('products/', product_views.product_list, name='products'),
]


