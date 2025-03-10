"""Create needed models and their admin."""

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    """Creates admin interface for Profile model."""

    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    """Create User's Admin."""

    inlines = [ProfileInline, ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
