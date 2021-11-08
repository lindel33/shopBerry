from django.contrib import messages
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, FormView, ListView


from .models import Order, OrderItem
from .forms import OrderForm
from cart.cart import Cart

class OrderUserCreate(CreateView):
    model = Order
    fields = OrderForm.Meta.fields
    template_name = 'main/order.html'
    success_url = '/'
    s = Cart.get_total_price
    extra_context = {'ex': s}


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            for item in cart:
                OrderItem.objects.create(order=form,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'main/order.html',
                          {'cart': form})
    else:
        form = OrderForm(request.POST)
    return render(request, 'main/order.html',
                  {'cart': cart, 'form': form})


class MakeOrderView(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        self.cart = Cart(request)

        if form.is_valid():
            new_order = form
            new_order.first_name = form.fields.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.comment = form.cleaned_data['comment']

            new_order.list_order = self.cart
            messages.add_message(request, messages.INFO, 'Спасибо за заказ! Менеджер с Вами свяжется')
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')


def req(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            cart = Cart(request.POST)
            return render(request, 'main/order.html', {'cart': cart})

    return render(request, 'main/order.html')