from django.urls import path

from products.views import products  # Controllers

app_name = 'products'  # App name

urlpatterns = [
    path('', products, name='index'),
]
