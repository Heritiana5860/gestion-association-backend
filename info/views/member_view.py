from rest_framework import viewsets, filters
from django.db.models import Count, Q, Prefetch
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from info.models import Member, Cotisation
from info.serializers import MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    # queryset = Member.objects.prefetch_related('cotisations').all().order_by('full_name')
    serializer_class = MemberSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['statut', 'level', 'is_inside']
    search_fields = ['full_name', 'number_phone', 'school', 'cde', 'address']
    
    def get_queryset(self):
        # Base de la requête
        queryset = Member.objects.all().order_by('full_name')
        year = self.request.query_params.get('year')
        
        if year:
            queryset = queryset.filter(cotisations__year=year).distinct()
            
            queryset = queryset.prefetch_related(
                Prefetch(
                    'cotisations',
                    queryset=Cotisation.objects.filter(year=year)
                )
            )
        else:
            queryset = queryset.prefetch_related('cotisations')
            
        return queryset
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        stats = Member.objects.aggregate(
            total=Count('id'),
            novices=Count('id', filter=Q(statut="NOVICE")),
            anciens=Count('id', filter=Q(statut="ANCIEN(NE)")),
            doyens=Count('id', filter=Q(statut="DOYEN(NE)")),
        )
        
        total = stats['total'] or 1
        stats['novices_percentage'] = (stats['novices'] * 100) / total
        stats['anciens_percentage'] = (stats['anciens'] * 100) / total
        stats['doyens_percentage'] = (stats['doyens'] * 100) / total
        
        return Response(stats)