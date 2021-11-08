from django.test import TestCase, Client
from django.contrib.auth import get_user_model


User = get_user_model()


class ShopTestCases(TestCase):

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
