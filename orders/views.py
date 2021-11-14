from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.forms import inlineformset_factory
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from baskets.models import Basket
from orders.models import Order, OrderItem
from orders.forms import OrderItemForm


class OrderList(ListView):
    model = Order
    extra_context = {'title': 'GeekShop - Заказы'}

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderItemsCreate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:orders_list')

    def get_context_data(self, **kwargs):
        data = super(OrderItemsCreate, self).get_context_data(**kwargs)
        order_formset = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        if self.request.POST:
            formset = order_formset(self.request.POST)
        else:
            basket_items = Basket.objects.filter(user=self.request.user)
            if len(basket_items):
                order_formset = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=len(basket_items))
                formset = order_formset()
                for num, form in enumerate(formset.forms):
                    form.initial.update({
                        'product': basket_items[num].product,
                        'quantity': basket_items[num].quantity,
                    })
                    # form.initial['product'] = basket_items[num].product
                    # form.initial['quantity'] = basket_items[num].quantity
                basket_items.delete()
            else:
                formset = order_formset()
        data['orderitems'] = formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        order_items = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if order_items.is_valid():
                order_items.instance = self.object
                order_items.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super(OrderItemsCreate, self).form_valid(form)


class OrderItemsUpdate(UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:orders_list')

    def get_context_data(self, **kwargs):
        data = super(OrderItemsUpdate, self).get_context_data(**kwargs)
        order_formset = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        if self.request.POST:
            data['orderitems'] = order_formset(self.request.POST, instance=self.object)
        else:
            data['orderitems'] = order_formset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        order_items = context['orderitems']

        with transaction.atomic():
            self.object = form.save()
            if order_items.is_valid():
                order_items.instance = self.object
                order_items.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super(OrderItemsUpdate, self).form_valid(form)


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:orders_list')


class OrderRead(DetailView):
    model = Order
    extra_context = {'title': 'заказ/просмотр'}
