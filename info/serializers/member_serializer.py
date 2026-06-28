from rest_framework import serializers
from ..models import Member, Cotisation

class CotisationInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotisation
        fields = ['id', 'year', 'amount', 'is_paid', 'payment_date']

class MemberSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)
    cotisations = serializers.SerializerMethodField()
    
    class Meta:
        model = Member
        fields = ['id', 'full_name', 'number_phone', 'is_inside', 'cde', 'address', 'school', 'level', 'statut', 'created_at', 'cotisations']
        
    def get_cotisations(self, obj):
        request = self.context.get('request')
        year = request.query_params.get('year') if request else None

        # Récupère les cotisations prefetchées (filtrées ou non)
        cotisations_list = getattr(obj, 'filtered_cotisations', None)
        if cotisations_list is None:
            cotisations_list = list(obj.cotisations.all())

        if year:
            if cotisations_list:
                return CotisationInlineSerializer(cotisations_list, many=True).data

            # Aucune cotisation pour cette année → valeurs par défaut
            return [{
                "id": None,
                "year": str(year),
                "amount": "0.00",
                "is_paid": False,
                "payment_date": None
            }]

        return CotisationInlineSerializer(cotisations_list, many=True).data