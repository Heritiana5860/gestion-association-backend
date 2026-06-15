from rest_framework import viewsets
from info.models import Honneur
from info.serializers import HonneurSerializer

class HonneurViewSet(viewsets.ModelViewSet):
    queryset = Honneur.objects.all()
    serializer_class = HonneurSerializer