from django.shortcuts import render

from .models import Entry
# Create your views here.

def index(request):
    """The home page for the site."""
    entries = Entry.objects.order_by('-date_added')
    context = {'entries':entries}
    return render(request, 'main_site/index.html', context)

def entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    context = {'entry':entry}
    return render(request, 'main_site/entry.html', context)

def pyprojects(request):
    return render(request, 'main_site/python.html')

def jsprojects(request):
    return render(request, 'main_site/javascript.html')