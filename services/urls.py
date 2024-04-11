from django.urls import path
from . import views 
from .views import get_types


urlpatterns = [
    path('', views.category_list, name = 'category_list'),
    path('service/<cat>', views.service_list, name='service_list'),
    path('add_service/', views.add_service, name='add_service'),
    path('get_types/<int:category_id>/', views.get_types, name='get_types'),
    path("login/", views.login_page, name = 'login_page')
]
