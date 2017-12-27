from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Entry, CodeEntry
from .forms import EntryForm, CodeEntryForm

def index(request):
    """The home page for the site."""
    index_entries = Entry.objects.order_by('-date_added')
    code_entries = CodeEntry.objects.order_by('-date_added')
    entries = list(index_entries) + list(code_entries)
    entries.sort(key=lambda x: x.date_added, reverse=True)
    context = {'entries':entries}
    return render(request, 'main_site/index.html', context)

def entry(request, entry_id):
    """A single entry."""
    entry = Entry.objects.get(id=entry_id)
    context = {'entry':entry}
    return render(request, 'main_site/entry.html', context)

def new_entry(request):
    """Add a new entry."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = EntryForm()
    else:
        #POST data submitted; create a blank form.
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_site:index'))
    
    context = {'form':form}
    return render(request, 'main_site/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    
    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        #POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_site:entry', args=[entry.id]))
    
    context = {'entry':entry, 'form':form}
    return render(request, 'main_site/edit_entry.html', context)

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

def new_code_entry(request):
    """Add a new code entry."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = CodeEntryForm()
    else:
        #POST data submitted; create a blank form.
        form = CodeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_site:index'))
    
    context = {'form':form}
    return render(request, 'main_site/new_code_entry.html', context)

def edit_code_entry(request, code_entry_id):
    """Edit an existing code entry."""
    code_entry = CodeEntry.objects.get(id=code_entry_id)

    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry.
        form = CodeEntryForm(instance=code_entry)
    else:
        #POST data submitted; process data.
        form = CodeEntryForm(instance=code_entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_site:code_entry', args=[code_entry.id]))

    context = {'code_entry':code_entry, 'form':form}
    return render(request, 'main_site/edit_code_entry.html', context)

def to_do(request):
    return render(request, 'main_site/to-do.html')