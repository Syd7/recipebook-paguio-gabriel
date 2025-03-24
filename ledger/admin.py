"""Create needed models and their admin."""

from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage


class IngredientAdmin(admin.ModelAdmin):
    """Create admin for Ingredient."""

    model = Ingredient


class RecipeImageInline(admin.StackedInline):
    """Create inline admin for RecipeImage"""

    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    """Create admin for Recipe."""

    model = Recipe
    inlines = [RecipeImageInline,]


class RecipeIngredientAdmin(admin.ModelAdmin):
    """Create admin for RecipeIngredient."""

    model = RecipeIngredient


# Register your models here.
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
