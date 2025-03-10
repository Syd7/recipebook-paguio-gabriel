"""Receives web requests and returns the necessary web response."""
from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required


def index(request):
    """Return index html file with apt context."""
    return render(request, 'index.html')


def recipe_list(request):
    """Return recipe_list html file with apt context."""
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes,
    }
    return render(request, 'recipe_list.html', ctx)


@login_required
def recipe_details(request, id):
    """Return recipe_details html file with apt context."""
    recipe = Recipe.objects.get(id=id)
    ctx = {
        "recipe": recipe
    }
    return render(request, 'recipe_details.html', ctx)
