from django.db import models

class AdhesionAnnuel(models.Model):
    adhasion_annuel_novice_in = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    adhasion_annuel_novice_ext = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    doyen_ancien_in = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    doyen_ancien_ext = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    year = models.IntegerField(unique=True)
    
    created_at = models.DateField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.year)