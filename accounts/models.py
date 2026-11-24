from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        LECTURER = 'LECTURER', 'Lecturer'
        TECHNICIAN = 'TECHNICIAN', 'IT Technician'
        IT_ADMIN = 'IT_ADMIN', 'IT Administrator'
        SYSTEM_ADMIN = 'SYSTEM_ADMIN', 'System Administrator'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT
    )


class UserProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    department = models.CharField(
        max_length=100,
        blank=True
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    registration_number = models.CharField(
        max_length=30,
        unique=True,
        null=True,
        blank=True
    )

    staff_id = models.CharField(
        max_length=30,
        unique=True,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Create your models here.
