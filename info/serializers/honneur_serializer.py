from rest_framework import serializers
from info.models import Honneur

class HonneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honneur
        fields = ['id', 'nom', 'fonction', 'contact', 'year', 'address']