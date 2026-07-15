from django.db import models

class Material(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    created_at = models.DateField(auto_now_add=True)
    is_update = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nom