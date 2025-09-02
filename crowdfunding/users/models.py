from django.contrib.auth.models import AbstractUser

from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('participant', 'Participant'),  # schools, groups, organizations
        ('donor', 'Donor'),
        ('sponsor', 'Sponsor'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='donor')

    def __str__(self):
        return self.username
