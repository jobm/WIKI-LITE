from django.conf.urls import url, include
from django.contrib import admin
from Wiki import views
urlpatterns = [
    url(r'',views.home),
    url(r'wiki/$',views.wiki),
]