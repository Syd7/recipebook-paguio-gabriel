"""Create needed models and their admin."""

from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    """Create admin for IngredientAdmin."""

    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    """Create admin for RecipeAdmin."""

    model = Recipe


class RecipeIngredientAdmin(admin.ModelAdmin):
    """Create admin for RecipeIngredientAdmin."""

    model = RecipeIngredient


# Register your models here.
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
