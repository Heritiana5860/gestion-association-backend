from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from info.serializers import CotisationSerializer
from info.models import Cotisation, Member, AdhesionAnnuel
from django.db import transaction
from django.db.models import Count, Q
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class CotisationViewSet(viewsets.ModelViewSet):
    # queryset = Cotisation.objects.all()
    serializer_class = CotisationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_paid', 'year']
    search_fields = ['member__full_name', 'member__cde', 'member__number_phone']
    
    def get_queryset(self):
        queryset = Cotisation.objects.all()
        year = self.request.query_params.get('year') 
        if year:
            queryset = queryset.filter(year=year)
        return queryset
    
    @action(detail=False, methods=['post'])
    def add(self, request):
        
        member_id = request.data.get('member_id')
        amount = request.data.get('amount')
        year = request.data.get('year')
        
        if not year:
            raise ValidationError({"year": "L'année est obligatoire pour attribuer une cotisation."})
        
        member = get_object_or_404(Member, id=member_id)
        
        tarifs = AdhesionAnnuel.objects.first()
        
        if not tarifs:
            raise ValidationError({"error": "Les tarifs annuels ne sont pas encore configurés."})
        
        if member.statut == 'NOVICE':
            target_amount = tarifs.adhasion_annuel_novice_in if member.is_inside else tarifs.adhasion_annuel_novice_ext
        elif member.statut in ['ANCIEN(NE)', 'DOYEN(NE)']:
            target_amount = tarifs.doyen_ancien_in if member.is_inside else tarifs.doyen_ancien_ext
        else:
            raise ValidationError({"error": f"Statut '{member.statut}' non reconnu."})
        
        if amount > target_amount:
            raise ValidationError({
                "amount": f"Le montant ({amount}) dépasse le tarif autorisé ({target_amount})"
            })
        
        with transaction.atomic():
            cotisation, created = Cotisation.objects.get_or_create(
                member=member,
                year=year,
                defaults={
                    'amount': amount,
                    'is_paid': (amount == target_amount)
                    }
            )
            
            if not created:
                cotisation.amount = amount
                cotisation.is_paid = (amount == target_amount)
                cotisation.save()

        return Response({
            "status":"created" if created else "updated", 
            "cotisation": self.get_serializer(cotisation).data
            })
           
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        year = request.query_params.get('year')
        
        cotisation_filter = Q()
        member_filter = Q()
        
        if year:
            cotisation_filter &= Q(year=year)
            member_filter &= Q(cotisations__year=year)
        
        novices = Member.objects.filter(member_filter & Q(statut="NOVICE")).distinct().count()
        anciens = Member.objects.filter(member_filter & Q(statut="ANCIEN(NE)")).distinct().count()
        doyens = Member.objects.filter(member_filter & Q(statut="DOYEN(NE)")).distinct().count()
        
        stats = Cotisation.objects.filter(cotisation_filter).aggregate(
            total=Count('id'),
            paid=Count('id', filter=Q(is_paid=True)),
            not_paid=Count('id', filter=Q(is_paid=False)),
            novices_paid=Count('id', filter=Q(member__statut="NOVICE", is_paid=True)),
            novices_not_paid=Count('id', filter=Q(member__statut="NOVICE", is_paid=False)),
            anciens_paid=Count('id', filter=Q(member__statut="ANCIEN(NE)", is_paid=True)),
            anciens_not_paid=Count('id', filter=Q(member__statut="ANCIEN(NE)", is_paid=False)),
            doyens_paid=Count('id', filter=Q(member__statut="DOYEN(NE)", is_paid=True)),
            doyens_not_paid=Count('id', filter=Q(member__statut="DOYEN(NE)", is_paid=False)),
        )
        
        total = stats['total'] or 0
        stats['paid_percentage'] = (stats['paid'] * 100) / total if total > 0 else 0
        stats['not_paid_percentage'] = (stats['not_paid'] * 100) / total if total > 0 else 0
        stats['novices_paid_percentage'] = (stats['novices_paid'] * 100) / novices if novices > 0 else 0
        stats['novices_not_paid_percentage'] = (stats['novices_not_paid'] * 100) / novices if novices > 0 else 0
        stats['anciens_paid_percentage'] = (stats['anciens_paid'] * 100) / anciens if anciens > 0 else 0
        stats['anciens_not_paid_percentage'] = (stats['anciens_not_paid'] * 100) / anciens if anciens > 0 else 0
        stats['doyens_paid_percentage'] = (stats['doyens_paid'] * 100) / doyens if doyens > 0 else 0
        stats['doyens_not_paid_percentage'] = (stats['doyens_not_paid'] * 100) / doyens if doyens > 0 else 0
        
        return Response(stats)        
    
    @action(detail=False, methods=['patch'])
    def reset(self, request):
        year = request.data.get('year')
        
        Cotisation.objects.filter(year=year).update(amount=0)
        
        return Response({"status": "all amount reset"})