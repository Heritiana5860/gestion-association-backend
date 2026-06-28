from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from info.models import Cotisation, Member, AdhesionAnnuel

@receiver(post_save, sender=Member)
def create_initial_cotisation(sender, instance, created, **kwargs):
    if created:
        # On récupère la configuration annuelle la plus récente
        tarifs_actifs = AdhesionAnnuel.objects.order_by('-year').first()
        
        # Si aucune configuration n'existe encore, on se rabat sur l'année système courante
        from django.utils import timezone
        target_year = tarifs_actifs.year if tarifs_actifs else timezone.now().year
        
        # On crée automatiquement la cotisation pour l'année en cours
        Cotisation.objects.get_or_create(
            member=instance,
            year=target_year,
            amount=0,
            is_paid=False
        )