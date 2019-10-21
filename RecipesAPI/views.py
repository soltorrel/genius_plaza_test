from rest_framework import viewsets
from .models import Recipe, Step, Ingredient
from .serializers import RecipeSerializer, StepSerializer, IngredientSerializer


class RecipesView(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class StepsView(viewsets.ModelViewSet):
    serializer_class = StepSerializer
    queryset = Step.objects.all()


class IngredientsView(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
