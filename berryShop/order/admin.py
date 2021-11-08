from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('update_at',)



