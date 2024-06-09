from django.shortcuts import render

from products.models import ProductCategory, Product


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
