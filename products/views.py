from django.shortcuts import render

from os import path
from json import load

# Create your views here.

MODULE_DIR = path.dirname(__file__)


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    file_path = path.join(MODULE_DIR, 'fixtures/goods.json')
    with open(file_path, encoding='utf-8') as f:
        products_list = load(f)
    context = {
        'title': 'GeekShop - Каталог',
        'header': 'GeekShop',
        'products': products_list
    }
    return render(request, 'products/products.html', context)
