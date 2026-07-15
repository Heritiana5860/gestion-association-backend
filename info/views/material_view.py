from info.serializers import MaterialSerializer
from info.models import Material
from rest_framework import viewsets

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer