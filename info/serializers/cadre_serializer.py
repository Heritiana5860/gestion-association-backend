from rest_framework import serializers
from info.models import Cadre

class CadreSerializer(serializers.ModelSerializer):
    added_at = serializers.DateField(read_only=True)
    
    class Meta:
        model = Cadre
        fields = ['id', 'nom', 'fonction', 'contact', 'address', 'added_at']