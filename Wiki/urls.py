from django.conf.urls import url, include
from django.contrib import admin
from Wiki import views
urlpatterns = [
    url(r'^$',views.home),
    url(r'wikis/$',views.wikis),

    url(r'wiki/(?P<pk>\d+)/$',views.wiki_view),

    url(r'wiki/create/$', views.wiki_add_form),
    url(r'wiki/add/$', views.wiki_create),

    url(r'wiki/edit/(?P<pk>\d+)/$', views.wiki_edit_form),
    url(r'wiki/update/$', views.wiki_update),
    url(r'wiki/delete/$', views.wiki_delete),
]