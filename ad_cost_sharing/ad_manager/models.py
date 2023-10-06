from django.db import models

class AdType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class AdRecord(models.Model):
    ad_type = models.CharField(max_length=10) 
    date = models.DateField()
    ads_run = models.PositiveIntegerField()
    actual_spend = models.DecimalField(max_digits=10, decimal_places=2)
    cost_sharing = models.DecimalField(max_digits=10, decimal_places=2)
    reimbursement = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.ad_type} - {self.date}"
    
    def save(self, *args, **kwargs):
        self.reimbursement = self.calculate_reimbursement()
        super().save(*args, **kwargs)

    def calculate_reimbursement(self):
        return self.actual_spend - self.cost_sharing
