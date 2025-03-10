"""Create app Accounts."""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Create app Accounts and assign name and details."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
