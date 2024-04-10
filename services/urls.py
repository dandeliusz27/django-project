from django.urls import path
from . import views 

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('service/<cat>', views.service_list, name='service_list'),
    path('add_service/', views.add_service, name='add_service'),
]
