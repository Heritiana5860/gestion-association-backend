from rest_framework import serializers
from info.models import President

class PresidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = President
        fields = ['id', 'nom', 'contact', 'year', 'bio']