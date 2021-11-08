from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from .models import Product, Category

User = get_user_model()


class ShopTestCases(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(
            id='100',
            name='ТестИмя',
            text='Описание',
            number='12',
            image_1=None,
            image_2=None,
            price='1200',
            discount='0',
            slug='test_slug',

        )
        self.category = Category.objects.create(
            name='ТестКатегория'

        )

    def test_create_product(self):
        self.assertEqual('ТестИмя', self.product.name)
        self.assertEqual('Описание', self.product.text)
        self.assertEqual('12', self.product.number)
        self.assertEqual(None, self.product.image_1)
        self.assertEqual(None, self.product.image_2)
        self.assertEqual('1200', self.product.price)
        self.assertEqual('0', self.product.discount)
        self.assertEqual('test_slug', self.product.slug)

    def test_create_category(self):
        self.assertEqual('ТестКатегория', self.category.name)

    def test_post_url_head(self):
        """
        Наличие главной страницы
        :return:
        """
        c = Client()
        response = c.get('/head')
        self.assertEqual(response.status_code, 200)

    def test_post_url_cart(self):
        """
        Наличие корзины
        :return:
        """
        c = Client()
        response = c.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_post_creati(self):
        """
        Наличие страницы доставки
        :return:
        """
        c = Client()
        response = c.get('/delivery')
        self.assertEqual(response.status_code, 200)

