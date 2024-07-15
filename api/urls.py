from django.urls import path

from api.views import ProductListAPIView

app_name = 'api'  # App name

urlpatterns = [
    path('product-list/', ProductListAPIView.as_view(), name='product_list'),
]
