from decimal import Decimal

import requests

from django.db import models
from shop.models import Product


class Order(models.Model):

    first_name = models.CharField('Имя', max_length=15,null=True)
    last_name = models.CharField('Фамилия', max_length=20,null=True)
    address = models.CharField('Адресс доставки', max_length=50,null=True)
    phone = models.SmallIntegerField('Телефон',null=True)
    email = models.EmailField('Email',null=True)
    comment = models.TextField('Комментарий', max_length=400,null=True)
    list_order = models.TextField('Список товаров', max_length=4000,null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
