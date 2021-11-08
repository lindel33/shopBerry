from django.urls import path, include
from .views import OrderUserCreate, order_create, MakeOrderView, req


urlpatterns = [
    path('orderbuy', OrderUserCreate.as_view(), name='order_buy'),
    path('make_order', MakeOrderView.as_view(), name='make_order'),
]
