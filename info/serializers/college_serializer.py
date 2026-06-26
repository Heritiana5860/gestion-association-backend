from rest_framework import serializers
from info.models import College

class CollegeSerializers(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'nom', 'contact', 'address', 'etablissement', 'niveau', 'nom_promotion', 'year']