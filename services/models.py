# lulu/models.py

from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
