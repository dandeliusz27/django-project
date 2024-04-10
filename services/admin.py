from django.contrib import admin

# Register your models here.
from .models import Category, Service, Type

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Type)