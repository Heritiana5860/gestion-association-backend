from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from info.models import Event, Member
from info.serializers import EventSerializer
from datetime import datetime
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = ['event_name', 'event_date', 'year']
    
    @action(detail=True, methods=['post'])
    def add_coming_member(self, request, pk=None):
        event = self.get_object()
        
        member_id = request.data.get('member_id')
        
        try:
            member = Member.objects.get(id= member_id)
            event_date = event.event_date
            event_start_time = event.event_start_time
            event_end_time = event.event_end_time
            
            current_date = datetime.now().date()
            current_time = datetime.now().time()
            
            if event_date != current_date:
                if event_date < current_date:
                    return Response({"Closed": "Event is already closed"})
                elif event_date > current_date:
                    return Response({"Closed": "Event is not yet open"})
                
            if event_date == current_date:
                if current_time < event_start_time.time():
                    return Response({"Closed": "It's not already time"})
                elif current_time > event_end_time.time():
                    return Response({"Closed": "It's done"})
            
            event.present_members.add(member)
            return Response({"status": "Member added"})
        except Member.DoesNotExist:
            return Response({"error": "Member not found"})
            
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