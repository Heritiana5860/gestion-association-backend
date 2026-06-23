from django.contrib import admin
from unfold.admin import ModelAdmin
from info.models import Member, Event, Cotisation, AdhesionAnnuel, President, Honneur, Cadre

@admin.register(Member)
class MemberAdmin(ModelAdmin):
    list_display = ['full_name', 'number_phone', 'statut', 'is_inside']
    list_filter = ['statut', 'is_inside', 'school']
    search_fields = ['full_name', 'number_phone', 'cde']
    
@admin.register(Cotisation)
class CotisationAdmin(ModelAdmin):
    list_display = ['member', 'year', 'is_paid', 'payment_date']
    list_filter = ['is_paid', 'member__statut']
    search_fields = ['member__full_name', 'member__cde', 'member__number_phone']
    
    actions = ['mark_as_paid']
    
    def mark_as_paid(self, request, queryset):
        queryset.update(is_paid=True)
    
@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ['event_name', 'event_date', 'event_start_time', 'event_end_time']
    list_filter = ['year']
    search_fields = ['event_name', 'event_date']
    
    fieldsets = (
        ('Infos générales', {
            'fields': ('event_name', 'event_description')
        }),
        ('Timing', {
            'fields': ('year' ,'event_date', 'event_start_time', 'event_end_time'),
        })
    )
    
@admin.register(AdhesionAnnuel)
class AdhesionAnnuelAdmin(ModelAdmin):
    list_display = ['year', 'created_at', 'is_updated']
    
@admin.register(President)
class PresidentAdmin(ModelAdmin):
    list_display = ['nom', 'contact', 'year']
    
@admin.register(Honneur)
class HonneurAdmin(ModelAdmin):
    list_display = ['nom', 'fonction', 'contact', 'year']
    
@admin.register(Cadre)
class HonneurAdmin(ModelAdmin):
    list_display = ['nom', 'fonction', 'contact', 'address']