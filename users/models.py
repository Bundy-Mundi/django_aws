from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [
      ('ML', 'Male'),
      ('FM', 'Female'),
      ('OT', 'Others')
    ]

    bio = models.TextField(default="")
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, default="")