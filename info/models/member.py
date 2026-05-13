from django.db import models

MEMBER_STATUT = [
    ("DOYEN(NE)", "Doyen(ne)"),
    ("ANCIEN(NE)", "Ancien(ne)"),
    ("NOVICE", "Novice(ne)"),
]

class Member(models.Model):
    full_name = models.CharField(max_length=200)
    number_phone = models.CharField(max_length=20)
    is_inside = models.BooleanField()
    address = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    statut = models.CharField(max_length=20, choices=MEMBER_STATUT, default="NOVICE")
    cde = models.CharField(max_length=100, unique=True)
    
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name