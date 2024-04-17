from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'bio']