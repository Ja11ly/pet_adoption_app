
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from pets.models import Pet

class AdoptionRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adoption_requests")
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="adoption_requests")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.pet.name} ({self.status})"
