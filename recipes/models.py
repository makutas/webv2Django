from django.db import models
from django.conf import settings


class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} (posted by {self.author})'


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    ingredient_type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'ingredients'

    def __str__(self):
        return f'{self.name}, {self.ingredient_type}'
