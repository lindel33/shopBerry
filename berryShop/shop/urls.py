from django.urls import path
from django.views.decorators.cache import cache_page

from .views import HomePage, DetailPage, delivery, Registr, about_view


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<int:pk>', DetailPage.as_view(), name='product_detail'),
    path('delivery', delivery, name='delivery'),
    path('registr/', Registr, name='registr'),
    path('about-us', about_view, name='about')

]
