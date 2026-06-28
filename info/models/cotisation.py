from django.db import models
from .member import Member

class Cotisation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="cotisations")
    year = models.CharField(blank=True, null=True, max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)
    
    payment_date = models.DateField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.member.full_name} - {self.year}"
    
    class Meta:
        unique_together = ('member', 'year')