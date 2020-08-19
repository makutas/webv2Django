from django.shortcuts import render


def index(request):
    """The home page for recipes"""
    return render(request, 'recipes/index.html')

