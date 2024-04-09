from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'name': "Justina"})

# lulu/views.py

from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})
