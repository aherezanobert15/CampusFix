from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'is_staff',
        'is_active',
    )

    list_filter = (
        'role',
        'is_staff',
        'is_active',
    )

    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )

    fieldsets = UserAdmin.fieldsets + (
        ('CampusFix Information', {
            'fields': ('role',)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('CampusFix Information', {
            'fields': ('role',)
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'department',
        'phone_number',
        'registration_number',
        'staff_id',
        'created_at',
    )

    search_fields = (
        'user__username',
        'user__email',
        'registration_number',
        'staff_id',
    )

    list_filter = ('department',)
