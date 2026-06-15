from django.db import models

class Honneur(models.Model):
    nom = models.TextField()
    fonction = models.TextField(blank=True, null=True)
    contact = models.CharField(blank=True, null=True)
    year = models.CharField(blank=True, null=True, max_length=20)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nom