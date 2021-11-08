from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
                path('admin/', admin.site.urls),
                path('cart', include('cart.urls', namespace='cart')),
                path('order/', include(('order.urls', 'order'), namespace='order')),
                path('', include(('shop.urls', 'shop'), namespace='shop')),
                path('accounts/', include('django.contrib.auth.urls')),
                url(r'^silk/', include('silk.urls', namespace='silk')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
