"""Create app Ledger."""

from django.apps import AppConfig


class LedgerConfig(AppConfig):
    """Create app Ledger and assign name and details."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ledger'
