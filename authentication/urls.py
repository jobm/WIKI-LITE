from authentication import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'contact/$', views.contact, name='contact'),
    url(r'about/$', views.about, name='about'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/', include('registration.backends.default.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
