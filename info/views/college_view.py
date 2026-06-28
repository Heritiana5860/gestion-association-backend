from rest_framework import viewsets
from info.serializers import CollegeSerializers
from info.models import College

class CollegeViewSets(viewsets.ModelViewSet):
    # queryset = College.objects.all()
    serializer_class = CollegeSerializers
    
    def get_queryset(self):
        queryset = College.objects.all()
        year = self.request.query_params.get('year') 
        if year:
            queryset = queryset.filter(year=year)
        return queryset