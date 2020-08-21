from django import forms
from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']
        labels = {'title': 'Title:', 'description': 'Description'}