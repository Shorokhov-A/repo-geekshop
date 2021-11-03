from django.urls import path

from products.views import ProductsListView, products

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('<category>/', products, name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='page'),
]
