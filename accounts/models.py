from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        RECEPTIONIST = "receptionist", "Receptionist"
        DOCTOR = "doctor", "Doctor"
        LAB_TECH = "lab_tech", "Laboratory Technician"
        PHARMACIST = "pharmacist", "Pharmacist"
        CASHIER = "cashier", "Cashier"
        MANAGER = "manager", "Manager"
        ADMIN = "admin", "System Administrator"

    role = models.CharField(max_length=20, choices=Role.choices)
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"
