from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')
