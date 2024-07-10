from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import (ProductsListView, basket_add,  # Controllers
                            basket_remove)

app_name = 'products'  # App name

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),

    # ../products/category/<category_id>
    path('category/<int:category_id>', ProductsListView.as_view(), name='category'),
    path('page/<int:page>', ProductsListView.as_view(), name='paginator'),

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),  # ../products/baskets/add/<product_id>/
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove')
]
