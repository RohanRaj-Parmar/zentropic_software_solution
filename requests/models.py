# requests/models.py
from django.db import models
from django.utils import timezone

class CustomerRequest(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('declined', 'Declined'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    service_type = models.CharField(max_length=50, choices=[
        ('website_design', 'Website Design'),
        ('web_app', 'Web Application'),
        ('mobile_app', 'Mobile App'),
        ('consultation', 'Consultation'),
        ('other', 'Other'),
    ])
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    timeline = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    admin_notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.service_type} ({self.created_at.strftime('%Y-%m-%d')})"
    
    class Meta:
        ordering = ['-created_at']