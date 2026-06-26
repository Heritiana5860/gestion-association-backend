from rest_framework import viewsets
from info.serializers import CollegeSerializers
from info.models import College

class CollegeViewSets(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializers