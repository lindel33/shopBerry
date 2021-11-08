from django.db import models


class Product(models.Model):

    name = models.CharField(verbose_name='Название', max_length=10, default='Клубника')
    text = models.TextField(verbose_name='Описание', max_length=2000, default='Текст')
    number = models.SmallIntegerField('Кол-во в коробке', default='1')
    image_1 = models.ImageField(verbose_name='Изображение 1', default=None)
    image_2 = models.ImageField(verbose_name='Изображение 2', default=None)
    price = models.SmallIntegerField(verbose_name='Цена', default='0')
    discount = models.SmallIntegerField(verbose_name='Скидка', default='0')
    slug = models.SlugField(verbose_name='Страница', unique=True, db_index=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Название', max_length=50, db_index=True)

    def __str__(self):
        return self.name



