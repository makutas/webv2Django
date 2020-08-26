from django import forms
from .models import Recipe, Ingredient, Quantity


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']
        labels = {'title': 'Title:', 'description': 'Description'}


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
        labels = {'name': 'Ingredient:', 'Type': 'ingredient_type'}


class QuantityForm(forms.ModelForm):
    class Meta:
        model = Quantity
        fields = ['ml_oz']
        labels = {'Ml:': 'ml_oz:'}