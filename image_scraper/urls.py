"""Defines URL patterns for the main_site."""

from django.conf.urls import url

from . import views

app_name = 'image_scraper'

urlpatterns = [
    # Home page
    url(r'^stories/$', views.stories, name='stories'),
]
