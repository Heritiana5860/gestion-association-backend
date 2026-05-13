from rest_framework import serializers
from ..models import Member

class MemberSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)
    
    class Meta:
        model = Member
        fields = ['id', 'full_name', 'number_phone', 'is_inside', 'cde', 'address', 'school', 'level', 'statut', 'created_at']