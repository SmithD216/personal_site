"""Defines URL patterns for the main_site."""

from django.conf.urls import url

from . import views

app_name = 'main_site'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    #Individual entry page
    url(r'^entries/(?P<entry_id>\d+)/$', views.entry, name='entry'),
]