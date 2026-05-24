from rest_framework import serializers
from info.models import Cotisation
from .member_serializer import MemberSerializer

class CotisationSerializer(serializers.ModelSerializer):
    payment_date = serializers.DateField(read_only=True)
    is_updated = serializers.DateTimeField(read_only=True)
    member = MemberSerializer(read_only=True)
    
    class Meta:
        model = Cotisation
        fields = ['id', 'member', 'year', 'amount', 'is_paid', 'payment_date', 'is_updated']