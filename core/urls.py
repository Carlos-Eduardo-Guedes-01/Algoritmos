from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produto/', include(('produto.urls', 'produto'), namespace='produto')),
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('empresa/', include(('empresa.urls', 'empresa'), namespace='empresa')),
    path('pacotes/', include(('pacotes.urls', 'pacotes'), namespace='pacotes')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)