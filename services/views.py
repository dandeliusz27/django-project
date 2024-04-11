from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User


from .models import Category, Type, Service

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def service_list(request, cat):
    services = Service.objects.filter(category=cat)
    return render(request, 'service_list.html', {'services': services})

def add_service(request):
    if request.method == "POST":
        category_id = request.POST['category']  # Poprawione
        type_id = request.POST['types']  # Poprawione
        user_id = request.user.id
        price_min = request.POST['price_min']
        price_max = request.POST['price_max']
        
        
        # Pobierz obiekty kategorii i typu na podstawie ich identyfikatorów
        category = Category.objects.get(id=category_id)
        type = Type.objects.get(id=type_id)
        
        # Utwórz nowy obiekt Service
        service = Service(category=category, types=type, user_id=user_id, price_min=price_min, price_max=price_max)  # Poprawione
        service.save()
        return redirect('category_list')  # Poprawiona przekierowanie do odpowiedniego widoku
    else:    
        categories = Category.objects.all()
        types = Type.objects.all()
        return render(request, 'add_service.html', {'categories': categories, 'types': types})
    

def get_types(request ,category_id):
    types = Type.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse({'types': list(types)})