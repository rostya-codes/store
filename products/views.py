from django.http import HttpResponseRedirect
from django.shortcuts import render

from products.models import ProductCategory, Product, Basket
from users.models import User


def handling_404(request, exception):
    return render(request, '404.html', {})


def index(request):
    """Products index controller"""
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)


def products(request):
    """Products products controller"""
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)


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
