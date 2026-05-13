from rest_framework import serializers
from info.models import Event, Member

class EventSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)
    present_members = serializers.PrimaryKeyRelatedField(many=True, queryset=Member.objects.all())
    
    class Meta:
        model = Event
        fields = ['id', 'event_name', 'event_description', 'event_date', 'event_start_time', 'event_end_time', 'present_members', 'year', 'created_at']