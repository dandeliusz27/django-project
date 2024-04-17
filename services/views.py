from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from services.forms import UserForm


from .models import Category, Type, Service, User

@login_required(login_url="/login")
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required(login_url="/login")
def service_list(request, id):
    services = Service.objects.filter(category=id)
    return render(request, 'service_list.html', {'services': services})

@login_required(login_url="/login")
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
    

def get_types(request, category_id):
    types = Type.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse({'types': list(types)})
    
@login_required(login_url="/login")
def get_my_profile(request):
    user = User.objects.get(id=request.user.id)
    services = Service.objects.filter(user = request.user.id)
    return render(request, 'profile.html', {'user': user, "services": services})

@login_required(login_url="/login")
def get_profile(request, id):
    user = User.objects.get(id=id)
    services = Service.objects.filter(user = id)
    return render(request, 'profile.html', {'user': user, "services": services})


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email = email)
        except:
            return
        
        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect("category_list")
    
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect('/login')

def register_page(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            login(request, user)

            return redirect("category_list")

    return render(request, 'register.html', {'form': form})