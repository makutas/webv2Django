from django.shortcuts import render
from .models import Recipe


def index(request):
    """The home page for recipes"""
    return render(request, 'recipes/index.html')


def recipes(request):
    """Show all recipes """
    recipes = Recipe.objects.order_by('created_date')
    context = {'recipes': recipes}
    return render(request, 'recipes/recipes.html', context)


def recipe(request, recipe_id):
    """Show a single recipe and all its ingredients"""
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = recipe.ingredient_set.order_by('ingredient_type')
    quantities = recipe.quantity_set.all()
    context = {'recipe': recipe, 'ingredients': ingredients, 'quantity': quantities}
    return render(request, 'recipes/recipe.html', context)