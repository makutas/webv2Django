from django.shortcuts import render, redirect
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm


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


def new_recipe(request):
    """Add a new recipe"""
    if request.method != 'POST':
        """Return blank form since no data is submitted - 'GET' method"""
        form = RecipeForm()
    else:
        """Process data since 'POST' method"""
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            form.save()
            new_recipe = Recipe.objects.latest('id')
            context = {'recipe': new_recipe, 'form': form}
            return redirect('new_ingredient', context)
    """Blank or invalid form"""
    context = {'form': form}
    return render(request, 'recipes/new_recipe.html', context)


def new_ingredient(request, recipe_id):
    """Add a new ingredient for particular recipe"""
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method != 'POST':
        """Return blank form since no data is submitted - 'GET' method"""
        form = IngredientForm()
    else:
        """Process data since 'POST' method"""
        form = IngredientForm(data=request.POST)
        if form.is_valid():
            new_ingredient_form = form.save(commit=False)
            new_ingredient_form.recipe = recipe
            new_ingredient_form.save()
            return redirect('recipes:recipe', recipe_id=recipe_id)
    """Blank or invalid form"""
    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipes/new_ingredient.html', context)


def edit_ingredient(request, ingredient_id):
    """Edit an existing ingredient"""
    ingredient = Ingredient.objects.get(id=ingredient_id)
    recipe = ingredient.recipe

    if request.method != 'POST':
        """Initial request; Pre-fill form with the current entry so the user can edit it"""
        form = IngredientForm(instance=ingredient)
    else:
        """POST data submitted; process data"""
        form = IngredientForm(instance=ingredient, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe', recipe_id=recipe.id)

    context = {'ingredient': ingredient, 'recipe': recipe, 'form': form}
    return render(request, 'recipes/edit_ingredient.html', context)


