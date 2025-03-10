"""Create model Profile appropriate fields."""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """Create model Profile with appropriate fields."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    biography = models.TextField(blank=True)
