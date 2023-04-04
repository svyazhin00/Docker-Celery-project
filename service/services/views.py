from django.db.models import Prefetch, F, Sum
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from services.models import *
from services.serializers import *


class SubscriptionsView(ReadOnlyModelViewSet):
    queryset = Subscriptions.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name',
                                                                                     'user__email'))
    ).annotate(price=F('service__full_price') -
                     (F('service__full_price') * F('plan__discount_percent')) / 100.00)
    serializer_class = SubscriptionsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        response_data = {'result': response.data}
        response.data = response_data
        response_data['total_amount'] = queryset.aggregate(total=Sum('price')).get('total')
        return response
