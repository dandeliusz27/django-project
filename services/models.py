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

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    types = models.ForeignKey(Type.objects.filter(category = category), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.category.name
   


