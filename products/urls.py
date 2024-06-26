from django.urls import path

from products.views import (ProductsListView, basket_add,  # Controllers
                            basket_remove)

app_name = 'products'  # App name

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>', ProductsListView.as_view(), name='category'),  # ../products/category/<category_id>
    path('page/<int:page>', ProductsListView.as_view(), name='paginator'),

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),  # ../products/baskets/add/<product_id>/
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove')
]
