from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for the site."""
    return render(request, 'main_site/index.html')