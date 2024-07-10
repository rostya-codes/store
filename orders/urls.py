from django.urls import path

from orders.views import OrderCreateView

app_name = 'orders'  # App name

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
]
