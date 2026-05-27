from django.db import models
from .member import Member

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.TextField(blank=True, null=True)
    event_date = models.DateField()
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField()
    
    present_members = models.ManyToManyField(Member, related_name="events_attended", blank=True, null=True)
    year = models.IntegerField()
    
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.event_name
    