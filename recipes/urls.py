"""Defines URL patterns for recipes"""

from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    # HOME PAGE
    path('', views.index, name='index'),
    # PAGE THAT SHOWS ALL RECIPES
    path('recipes/', views.recipes, name='recipes'),
    # DETAIL PAGE FOR A SINGLE RECIPE
    path('recipes/<int:recipe_id>', views.recipe, name='recipe'),
    # PAGE FOR ADDING A NEW RECIPE
    path('new_recipe/', views.new_recipe, name='new_recipe'),
]