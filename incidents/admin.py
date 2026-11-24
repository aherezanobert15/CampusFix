from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'reporter',
        'category',
        'priority',
        'status',
        'assigned_technician',
        'created_at',
    )

    list_filter = (
        'category',
        'priority',
        'status',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
        'reporter__username',
        'assigned_technician__username',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    ordering = ('-created_at',)
