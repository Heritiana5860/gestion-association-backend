from rest_framework import viewsets
from info.models import President
from info.serializers import PresidentSerializer

class PresidentViewSet(viewsets.ModelViewSet):
    queryset = President.objects.all().order_by('-year')
    serializer_class = PresidentSerializer