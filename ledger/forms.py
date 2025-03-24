"""Create forms with appropriate fields."""

from django import forms
from .models import RecipeImage, Recipe


class RecipeImageForm(forms.ModelForm):
    """Creates a form to update image of Recipe"""
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']


class RecipeForm(forms.ModelForm):
    """Creates a form to add details for the Recipe"""
    class Meta:
        model = Recipe
        fields = ['name']
