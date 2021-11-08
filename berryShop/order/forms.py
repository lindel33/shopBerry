from django import forms
from django.forms import ModelChoiceField

from .models import Order


from django.conf import settings


class OrderForm(forms.Form):

    class Meta:
        model = Order

        fields = ['list_order', 'first_name', 'last_name', 'address', 'phone', 'comment', 'email']



