from django.urls import path
from . import views 

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('service/', views.service_list, name='service_list'),
]
