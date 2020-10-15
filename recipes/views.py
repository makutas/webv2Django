from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient, Quantity
from .forms import RecipeForm, IngredientForm, QuantityForm


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
    ingredients = recipe.ingredient_set.all()
    quantities = recipe.quantity_set.all()
    zipped = zip(ingredients, quantities)
    context = {'recipe': recipe, 'ingredients': ingredients, 'quantities': quantities, 'zipped': zipped}
    return render(request, 'recipes/recipe.html', context)


@login_required
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
            recipe = Recipe.objects.last()
            recipe.author = request.user
            form = IngredientForm()
            context = {'recipe': recipe, 'form': form}
            return render(request, 'recipes/new_ingredient.html', context)
    """Blank or invalid form"""
    context = {'form': form}
    return render(request, 'recipes/new_recipe.html', context)


@login_required
def edit_recipe(request, recipe_id):
    recipe = Recipe.object.get(id=recipe_id)

    if request.method != 'POST':
        """Initial request; Pre-fill form with the current entry so the user can edit it"""
        form = RecipeForm()
    else:
        """POST data submitted; process data"""
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('recipes:recipe', recipe_id=recipe.id)

    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipes/edit_recipe.html', context)


@login_required
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
            ingredient = Ingredient.objects.last().id
            form = QuantityForm()
            context = {'recipe': recipe, 'ingredient': ingredient, 'form': form}
            return render(request, 'recipes/add_quantity.html', context)
    """Blank or invalid form"""
    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipes/new_ingredient.html', context)


@login_required
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


@login_required
def quantity(request, recipe_id, ingredient_id):
    """Add quantity for particular recipe and ingredient"""
    recipe = Recipe.objects.get(id=recipe_id)
    ingredient = Ingredient.objects.get(id=ingredient_id)

    if request.method != 'POST':
        """Return blank form since no data is submitted - 'GET' method"""
        form = QuantityForm()
    else:
        """Process data since 'POST' method"""
        form = QuantityForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.recipe = recipe
            form.ingredient = ingredient
            form.save()
            return redirect('recipes:recipe', recipe_id=recipe_id)
    """Blank or invalid form"""
    context = {'recipe': recipe, 'ingredient': ingredient, 'form': form}
    return render(request, 'recipes/add_quantity.html', context)


@login_required
def edit_quantity(request, recipe_id, ingredient_id):
    """Edit an existing ingredient"""
    recipe = Recipe.objects.get(id=recipe_id)
    ingredient = Ingredient.objects.get(id=ingredient_id)
    quantity = get_object_or_404(Quantity, recipe_id=recipe_id, ingredient_id=ingredient_id)

    if request.method != 'POST':
        """Initial request; Pre-fill form with the current entry so the user can edit it"""
        form = QuantityForm(instance=quantity)
    else:
        """POST data submitted; process data"""
        form = QuantityForm(request.POST, instance=quantity)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe', recipe_id=recipe.id)

    context = {'recipe': recipe, 'ingredient': ingredient, 'quantity': quantity, 'form': form}
    return render(request, 'recipes/edit_quantity.html', context)
