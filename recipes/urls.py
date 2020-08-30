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
    # PAGE FOR ADDING AN INGREDIENT
    path('new_ingredient/<int:recipe_id>/', views.new_ingredient, name='new_ingredient'),
    # PAGE FOR EDITING INGREDIENTS
    path('edit_ingredient/<int:ingredient_id>/', views.edit_ingredient, name='edit_ingredient'),
    # PAGE FOR ADDING QUANTITY
    path('recipes/<int:recipe_id>/<int:ingredient_id>/add_quantity', views.quantity, name='add_quantity'),
    # PAGE FOR EDITING QUANTITY
    path('recipes/<int:recipe_id>/<int:ingredient_id>/edit_quantity', views.edit_quantity, name='edit_quantity'),
]