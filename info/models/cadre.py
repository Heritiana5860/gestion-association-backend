from django.db import models

class Cadre(models.Model):
    nom = models.TextField()
    fonction = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    
    added_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nom