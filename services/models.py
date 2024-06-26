from django.contrib.auth.models import AbstractUser
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
    phone = models.TextField(max_length=200, null=True)
    location = models.TextField(max_length=200, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    types = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price_min = models.IntegerField(null=True)
    price_max = models.IntegerField(null=True)

    def __str__(self):
        return self.category.name




