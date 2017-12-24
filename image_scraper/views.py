from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def stories(request):
    return render(request, 'image_scraper/home.html')

