from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from services.models import *
from services.serializers import *

class SubscriptionsView(ReadOnlyModelViewSet):
    queryset = Subscriptions.objects.all().prefetch_related(
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name',
                                                              'user__email'))
    )
    serializer_class = SubscriptionsSerializer
