from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from django.db import transaction
from rest_framework.decorators import action
from rest_framework.response import Response
from info.models import AdhesionAnnuel
from info.serializers import AnnuelSerializer

class AdhasionAnnuelViewSet(viewsets.ModelViewSet):
    queryset = AdhesionAnnuel.objects.all()
    serializer_class = AnnuelSerializer
    filterset_fields = ['year']
    
    @action(detail=False, methods=['post'])
    def fix_statut_amount(self, request):
        
        year = request.data.get('year')
        novice_amount_in = request.data.get('novice_amount_inside')
        novice_amount_ext = request.data.get('novice_amount_outside')
        doyen_ancien_amount_in = request.data.get('doyen_ancien_amount_inside')
        doyen_ancien_amount_ext = request.data.get('doyen_ancien_amount_outside')
        
        errors = {}
        
        if not year:
            errors["year"] = "L'année doit être précisée."
            
        if errors:
            raise ValidationError(errors)
        
        with transaction.atomic():
            annuel, created = AdhesionAnnuel.objects.get_or_create(
                year=year,
                defaults={
                    "adhasion_annuel_novice_in": novice_amount_in,
                    "adhasion_annuel_novice_ext": novice_amount_ext,
                    "doyen_ancien_in": doyen_ancien_amount_in,
                    "doyen_ancien_ext": doyen_ancien_amount_ext,
                }
            )
            
            if not created:
                annuel.adhasion_annuel_novice_in = novice_amount_in
                annuel.adhasion_annuel_novice_ext = novice_amount_ext
                annuel.doyen_ancien_in = doyen_ancien_amount_in
                annuel.doyen_ancien_ext = doyen_ancien_amount_ext
                annuel.save()

        return Response({
            "status": "added" if created else "updated",
            "data": self.get_serializer(annuel).data
            })