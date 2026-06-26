from django.db import models

class College(models.Model):
    nom = models.TextField()
    contact = models.CharField(max_length=12)
    address = models.CharField(max_length=255)
    etablissement = models.CharField(max_length=100, blank=True, null=True)
    niveau = models.CharField(max_length=10)
    nom_promotion = models.CharField(max_length=150, blank=True, null=True)
    year = models.IntegerField()
    
    def __str__(self):
        return self.nom