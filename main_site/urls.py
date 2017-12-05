"""Defines URL patterns for the main_site."""

from django.conf.urls import url

from . import views

app_name = 'main_site'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
]