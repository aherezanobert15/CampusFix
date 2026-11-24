from django.db import models
from django.db import models
from django.conf import settings


class Incident(models.Model):

    class Category(models.TextChoices):
        WIFI = 'WIFI', 'Wi-Fi'
        NETWORK = 'NETWORK', 'Network'
        HARDWARE = 'HARDWARE', 'Hardware'
        SOFTWARE = 'SOFTWARE', 'Software'
        LAB_COMPUTER = 'LAB_COMPUTER', 'Laboratory Computer'
        ACCOUNT = 'ACCOUNT', 'Account Access'
        OTHER = 'OTHER', 'Other'

    class Priority(models.TextChoices):
        LOW = 'LOW', 'Low'
        MEDIUM = 'MEDIUM', 'Medium'
        HIGH = 'HIGH', 'High'
        URGENT = 'URGENT', 'Urgent'

    class Status(models.TextChoices):
        NEW = 'NEW', 'New'
        ASSIGNED = 'ASSIGNED', 'Assigned'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        RESOLVED = 'RESOLVED', 'Resolved'
        CLOSED = 'CLOSED', 'Closed'

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER
    )

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW
    )

    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reported_incidents'
    )

    assigned_technician = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_incidents'
    )
    resolution_notes = models.TextField(
    blank=True,
    null=True,
    help_text="Explanation of how the incident was resolved."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
# Create your models here
