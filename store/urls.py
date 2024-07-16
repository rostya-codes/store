from debug_toolbar.toolbar import debug_toolbar_urls
# Импорт файла settings правильно делать так, чтобы подтянулись все внутренние настройки
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken.views import obtain_auth_token

from orders.views import stripe_webhook_view
from products.views import IndexView

handler404 = 'common.views.handling_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(extra_context={'title': 'Store'}), name='index'),  # Main page
    # allauth
    path('accounts/', include('allauth.urls')),
    # apps
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),
    path('api/', include('api.urls', namespace='api')),
    path('api-token-auth/', obtain_auth_token),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
