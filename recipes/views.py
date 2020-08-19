from django.shortcuts import render
from .models import Recipe


def index(request):
    """The home page for recipes"""
    return render(request, 'recipes/index.html')


def recipes(request):
    """Show all recipes """
    recipes = Recipe.objects.order_by('created_date')
    context = {'recipes':recipes}
    return render(request, 'recipes/recipes.html', context)

