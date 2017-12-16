from django.contrib import admin

# Register your models here.

from main_site.models import Entry, CodeEntry

admin.site.register(Entry)
admin.site.register(CodeEntry)