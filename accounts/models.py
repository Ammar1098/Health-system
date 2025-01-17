from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Unique related name for custom User model
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Unique related name for custom User model
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user'
    )

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
