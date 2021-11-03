from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.models import ProductCategory, Product

# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop'
        context['header'] = 'GeekShop Store'
        return context


def products(request, category_id=None, page=1):
    context = {
        'title': 'GeekShop - Каталог',
        'header': 'GeekShop',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products_list = Product.objects.filter(category_id=category_id)
    else:
        products_list = Product.objects.all()
    paginator = Paginator(products_list, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)


# def index(request):
#     context = {
#         'title': 'GeekShop',
#         'header': 'GeekShop Store',
#     }
#     return render(request, 'products/index.html', context)
