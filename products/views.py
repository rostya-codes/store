from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from products.models import ProductCategory, Product, Basket


def handling_404(request, exception):
    """404 page handling controller"""
    return render(request, '404.html', {})


class IndexView(TemplateView):
    """ Home page controller """

    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        """Returns context data"""
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context


class ProductsListView(ListView):
    """ Products page controller """

    model = Product  # Определяется тут, а не в get_context_data
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')  # Если по ключу значения нет, то будет присвоено None
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['title'] = 'Store - Каталог'
        context['categories'] = ProductCategory.objects.all()
        return context


@login_required
def basket_add(request, product_id):
    """Basket add controller"""
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])  # Та страница на которой находится пользователь


@login_required
def basket_remove(request, basket_id):
    """Basket remove controller"""
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
