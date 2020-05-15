from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    images = Product.objects.get(pk=1)
    return render(request, 'home/home.html', {'images': images,})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    render(request, 'home/contact.html')