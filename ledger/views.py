from django.shortcuts import render
from .models import Recipe

def index(request):
    return render(request, 'index.html', ctx)

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes,
        
}
    return render(request, 'recipe_list.html', ctx)
    
def recipe_details(request, id):
    recipe = Recipe.objects.get(id=id)
    ctx = {
        "recipe": recipe
    }
    return render(request, 'recipe_details.html', ctx)