from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


# Register your models here.
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
