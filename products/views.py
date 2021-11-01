from django.shortcuts import render
from products.models import ProductCategory, Product

# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    if category_id:
        products_list = Product.objects.filter(category_id=category_id)
    else:
        products_list = Product.objects.all()
    context = {
        'title': 'GeekShop - Каталог',
        'header': 'GeekShop',
        'categories': ProductCategory.objects.all(),
        'products': products_list,
    }
    return render(request, 'products/products.html', context)
