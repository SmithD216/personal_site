"""Defines URL patterns for the main_site."""

from django.conf.urls import url

from . import views

app_name = 'main_site'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    #Individual entry page
    url(r'^entries/(?P<entry_id>\d+)/$', views.entry, name='entry'),
    #Page for adding a new entry
    url(r'^new_topic/$', views.new_entry, name='new_entry'),
    #Add an entry edit page here!
    #---
    #Python projects page
    url(r'^python/$', views.pyprojects, name='pyprojects'),
    #Javascript projects page
    url(r'^javascript/$', views.jsprojects, name='jsprojects'),
    #Individual project entry page
    url(r'^code_entries/(?P<code_entry_id>\d+)/$', views.code_entry, name='code_entry'),
]
