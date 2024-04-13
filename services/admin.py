from django.contrib import admin

# Register your models here.
from .models import Category, Service, Type, User

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Type)
admin.site.register(User)