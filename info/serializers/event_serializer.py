from rest_framework import serializers
from info.models import Event, Member
from .member_serializer import MemberSerializer

class EventSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)
    present_members = MemberSerializer(many=True, read_only=True)
    
    present_members_ids = serializers.PrimaryKeyRelatedField(
        source='present_members',
        many=True,
        queryset=Member.objects.all(),
        write_only=True,
        required=False,
    )
    
    class Meta:
        model = Event
        fields = ['id', 'event_name', 'event_description', 'event_date', 'event_start_time', 'event_end_time', 'present_members', 'present_members_ids', 'year', 'created_at']