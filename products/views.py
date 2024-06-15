from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products.models import ProductCategory, Product, Basket


def handling_404(request, exception):
    return render(request, '404.html', {})


def index(request):
    """Products index controller"""
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_number=1):
    """Products products controller"""
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    # Paginator
    per_page = 2
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator
    }
    return render(request, 'products/products.html', context)


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
