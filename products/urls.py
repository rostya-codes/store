from django.urls import path

from products.views import products, basket_add  # Controllers

app_name = 'products'  # App name

urlpatterns = [
    path('', products, name='index'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add')  # ../products/baskets/add/<product_id>/
]
