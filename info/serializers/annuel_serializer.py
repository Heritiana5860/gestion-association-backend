from rest_framework import serializers
from info.models import AdhesionAnnuel

class AnnuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdhesionAnnuel
        fields = ['id', 'year', 'adhasion_annuel_novice_in', 'adhasion_annuel_novice_ext', 'doyen_ancien_in', 'doyen_ancien_ext', 'created_at', 'is_updated']
        read_only_field = ['created_at', 'is_updated']