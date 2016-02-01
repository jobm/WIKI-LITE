from django.conf.urls import url, include
from django.contrib import admin
from Wiki import views

urlpatterns = [
    # url(r'^$', views.home),
    url(r"^$", views.wikis, name="wikis"),

    url(r'wiki/(?P<slug>\w+)/$', views.wiki_view, name="details"),

    url(r'wiki/create/$', views.wiki_add_form, name="create"),
    url(r"wiki/add/$", views.wiki_create, name="add"),

    url(r'wiki/edit/(?P<pk>\d+)/$', views.wiki_edit_form, name="edit"),
    url(r'wiki/update/(?P<pk>\d+)/$', views.wiki_update, name="update"),
    url(r'wiki/delete/(?P<pk>\d+)/$', views.wiki_delete, name="delete"),
]
