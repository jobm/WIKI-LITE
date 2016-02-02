from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from authentication import views

urlpatterns = [
    url(r'accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
