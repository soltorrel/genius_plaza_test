from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(null=False, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Step(models.Model):
    step_text = models.CharField(null=False, max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Ingredient(models.Model):
    text = models.CharField(null=False, max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

