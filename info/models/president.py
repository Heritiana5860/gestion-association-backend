from django.db import models

class President(models.Model):
    nom = models.TextField()
    contact = models.CharField(blank=True, null=True, max_length=20)
    year = models.CharField(blank=True, null=True, max_length=20)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nom