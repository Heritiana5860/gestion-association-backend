from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from info.models import Event, Member
from info.serializers import EventSerializer
from datetime import datetime
from django.utils import timezone
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-id')
    serializer_class = EventSerializer
    filterset_fields = ['event_name', 'event_date', 'year']
    
    @action(detail=True, methods=['post'])
    def add_coming_member(self, request, pk=None):
        now = timezone.now()
        event = self.get_object()
        
        member_cde = request.data.get('member_cde')
        
        try:
            member = Member.objects.get(cde= member_cde)
            event_date = event.event_date
            event_start_time = event.event_start_time
            event_end_time = event.event_end_time
            
            local_now = timezone.localtime(now)
            current_date = local_now.date()
            
            if event_date != current_date:
                if event_date < current_date:
                    return Response({"Closed": "L'événement est déjà clôturé"})
                elif event_date > current_date:
                    return Response({"Closed": "L'événement n'est pas encore ouvert"})
                
            if event_date == current_date:
                if now < event_start_time:
                    return Response({"Closed": "Fermé: Il n'est pas encore l'heure"})
                elif now > event_end_time:
                    return Response({"Fermé: C'est terminé"})
            
            if event.present_members.filter(pk=member.pk).exists():
                return Response({"status": "Membre déjà présent"})
            
            event.present_members.add(member)
            return Response({"status": "Membre ajouté"})
        except Member.DoesNotExist:
            return Response({"error": "Member introuvable"})
            
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        event_id = request.query_params.get('event_id')
        
        event = get_object_or_404(Event, id=event_id)
        
        member = Member.objects
        total_member = member.count()
        novices = member.filter(statut="NOVICE").count()
        anciens = member.filter(statut="ANCIEN(NE)").count()
        doyens = member.filter(statut="DOYEN(NE)").count()
        
        stats = event.present_members.aggregate(
            total_comming=Count('id'),
            novices=Count('id', filter=Q(statut="NOVICE")),
            anciens=Count('id', filter=Q(statut="ANCIEN(NE)")),
            doyens=Count('id', filter=Q(statut="DOYEN(NE)")),
        )
        
        total = stats['total_comming'] or 0
        stats['coming_pourcentage'] = (total * 100) / total_member if total_member > 0 else 0
        stats['novices_pourcentage'] = (stats['novices'] * 100) / novices if novices > 0 else 0
        stats['anciens_pourcentage'] = (stats['anciens'] * 100) / anciens if anciens > 0 else 0
        stats['doyens_pourcentage'] = (stats['doyens'] * 100) / doyens if doyens > 0 else 0
        
        return Response(stats)