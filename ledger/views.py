from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html') 

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes,
    }
    return render(request, 'recipe_list.html', ctx)

@login_required
def recipe_details(request, id):
    recipe = Recipe.objects.get(id=id)
    ctx = {
        "recipe": recipe
    }
    return render(request, 'recipe_details.html', ctx)