from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    ingredient_type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'ingredients'

    def __str__(self):
        return f'{self.name}, {self.ingredient_type}'


class Quantity(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ml_oz = models.IntegerField(max_length=5, null=True, blank=True)
    pieces = models.IntegerField(max_length=5, null=True, blank=True)
    dashes = models.IntegerField(max_length=5, null=True, blank=True)
    shake = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'quantities'

    def __str__(self):
        return f'{self.ml_oz}, {self.pieces}, {self.dashes}, {self.shake}'


