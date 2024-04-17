from django.urls import path
from . import views 


urlpatterns = [
    path('', views.category_list, name = 'category_list'),
    path('service/<id>', views.service_list, name='service_list'),
    path('add_service', views.add_service, name='add_service'),
    path('get_types/<category_id>/', views.get_types, name='get_types'),
    path("login", views.login_page, name = 'login_page'),
    path("logout", views.logoutUser, name = 'logout_user'),
    path("register", views.register_page, name = 'register_page'),
    path("profile/my/", views.get_my_profile, name = 'my_profile_page'),
    path("profile/<id>", views.get_profile, name = 'my_profile_page')
]
