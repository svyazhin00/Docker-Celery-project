from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    """Модель пользователя"""
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

