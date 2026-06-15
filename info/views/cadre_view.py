from rest_framework import viewsets
from info.serializers import CadreSerializer
from info.models import Cadre

class CadreViewSet(viewsets.ModelViewSet):
    queryset = Cadre.objects.all()
    serializer_class = CadreSerializer
        