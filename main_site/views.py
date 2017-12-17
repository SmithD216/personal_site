from django.shortcuts import render

from .models import Entry, CodeEntry
# Create your views here.

def index(request):
    """The home page for the site."""
    index_entries = Entry.objects.order_by('-date_added')
    code_entries = CodeEntry.objects.order_by('-date_added')
    entries = list(index_entries) + list(code_entries)
    entries.sort(key=lambda x: x.date_added, reverse=True)
    context = {'entries':entries}
    return render(request, 'main_site/index.html', context)

def entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    context = {'entry':entry}
    return render(request, 'main_site/entry.html', context)

def pyprojects(request):
    code_entries = CodeEntry.objects.order_by('-date_added')
    context = {'code_entries':code_entries}
    return render(request, 'main_site/python.html', context)

def jsprojects(request):
    code_entries = CodeEntry.objects.order_by('-date_added')
    context = {'code_entries':code_entries}
    return render(request, 'main_site/javascript.html', context)

def code_entry(request, code_entry_id):
    code_entry = CodeEntry.objects.get(id=code_entry_id)
    context = {'code_entry':code_entry}
    return render(request, 'main_site/code_entry.html', context)