from django.urls import path

from orders.views import (CanceledTemplateView, OrderCreateView,
                          SuccessTemplateView, OrderListView)

app_name = 'orders'  # App name

urlpatterns = [
    path('', OrderListView.as_view(), name='orders_list'),
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-cancel/', CanceledTemplateView.as_view(), name='order_cancel'),
]
