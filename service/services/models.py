from django.core.validators import MaxValueValidator
from django.db import models
from clients.models import *
class Services(models.Model):
    """Модель сервиса"""
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Plan(models.Model):
    """Модель тарифного плана"""
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
                )
    plan_type = models.CharField(choices=PLAN_TYPES, max_length=15)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                       MaxValueValidator(100)
                                                   ])
    def __str__(self):
        return self.plan_type
class Subscriptions(models.Model):
    """Модель подписок пользователей"""
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Services, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)

    def __str__(self):
        return f'Subscription {self.client} by service {self.service}'






