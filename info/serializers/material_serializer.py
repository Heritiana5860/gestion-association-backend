from info.models import Material
from rest_framework import serializers

class MaterialSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)
    is_update = serializers.DateField(read_only=True)
    
    class Meta:
        model = Material
        fields = ['id', 'nom', 'description', "nombre_materiel", 'created_at', 'is_update']