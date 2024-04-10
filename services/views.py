from django.shortcuts import render
from django.http import HttpResponse


from .models import Category, Service

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})