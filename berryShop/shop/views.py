from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product

from .forms import RegistrForm

from cart.forms import CartAddProductForm


class HomePage(ListView):

    queryset = Product.objects.values('id', 'image_1', 'name', 'price', 'discount', 'number')
    template_name = 'index.html'
    context_object_name = 'product_slug'


class DetailPage(DetailView):

    model = Product
    template_name = 'detailPage.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    cart_product_form = CartAddProductForm
    extra_context = {'cart_product_form': cart_product_form}


def delivery(request):
    return render(request, 'delivery.html')


# Функция регистрации
def Registr(request):
    data = {}
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Всё прошло успешно"
            return render(request, 'registration/registr.html', data)
    else:
        form = RegistrForm()
        data['form'] = form
        return render(request, 'registration/registr.html', data)


def about_view(request):
    return render(request, 'about.html')


class OrderView(DetailView):
    pass
