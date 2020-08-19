"""Defines URL patterns for recipes"""

from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    # HOME PAGE
    path('', views.index, name='index'),
    # PAGE THAT SHOWS ALL RECIPES
    path('recipes/', views.recipes, name='recipes'),
]