from django import forms
from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']
        labels = {'title': 'Title:', 'description': 'Description'}


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'ingredient_type']
        labels = {'name': 'Ingredient:', 'Type': 'ingredient_type'}