"""Create models with appropriate fields."""

from django.db import models
from django.urls import reverse

from accounts.models import Profile


# Create your models here.


class Ingredient(models.Model):
    """Create Ingredient with appropriate fields."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """Return name of the recipe."""
        return self.name

    def get_absolute_url(self):
        """Return absolute url of the recipe."""
        return reverse('ingredient_detail', args=[self.id])


class Recipe(models.Model):
    """Create Recipe with appropriate fields."""

    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now_add=True)
    last_update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return name of the recipe."""
        return self.name

    def get_absolute_url(self):
        """Return absolute url of the recipe."""
        return reverse('recipe_detail', args=[self.id])


class RecipeIngredient(models.Model):
    """Create RecipeIngredient with appropriate fields."""

    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients")
