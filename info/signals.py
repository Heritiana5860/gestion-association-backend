from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from info.models import Cotisation, Member

@receiver(post_save, sender=Member)
def create_initial_cotisation(sender, instance, created, **kwargs):
    if created:
        # On crée automatiquement la cotisation pour l'année en cours
        Cotisation.objects.create(
            member=instance,
            year=datetime.now().year,
            amount=0,
            is_paid=False
        )