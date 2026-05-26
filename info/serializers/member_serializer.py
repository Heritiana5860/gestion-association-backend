from rest_framework import serializers
from ..models import Member, Cotisation

class CotisationInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotisation
        fields = ['id', 'year', 'amount', 'is_paid', 'payment_date']

class MemberSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)
    cotisations = CotisationInlineSerializer(many=True, read_only=True)
    
    class Meta:
        model = Member
        fields = ['id', 'full_name', 'number_phone', 'is_inside', 'cde', 'address', 'school', 'level', 'statut', 'created_at', 'cotisations']