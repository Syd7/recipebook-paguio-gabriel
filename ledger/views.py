"""Receives web requests and returns the necessary web response."""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Recipe
from .forms import RecipeImageForm, RecipeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from accounts.models import Profile


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


@login_required
def add_image(request, pk):
    """Allows logged-in users to add an image to a recipe"""
    recipe = get_object_or_404(Recipe, id=pk)
    form = RecipeImageForm()
    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect("ledger:recipe_detail", id=recipe.id)
    ctx = {"form": form, "recipe": recipe}
    return render(request, 'add_image.html', {'form': form, 'recipe': recipe})


@login_required
def add_recipe(request):
    """Allows logged-in users to create a new recipe."""
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            # gets current user profile
            profile = Profile.objects.get(user=request.user)
            recipe.author = profile  # assigns it to author
            recipe.save()
            return redirect("ledger:recipe_list")
    return render(request, "add_recipe.html", {"form": form})
