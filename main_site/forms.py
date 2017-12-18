from django import forms

from .models import Entry, CodeEntry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']
        
class CodeEntryForm(forms.ModelForm):
    class Meta:
        model = CodeEntry
        fields = ['title']