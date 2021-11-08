from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('update_at',)


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show', 'price', 'discount']
    prepopulated_fields = {"slug": ('name',)}

    exclude = ('updated_at',)

    def image_show(self, obj):
        if obj.image_1:
            return mark_safe("<img src='{}' width='60' />".format(obj.image_1.url))
        return 'None'

    image_show.__name__ = "Картинка"

