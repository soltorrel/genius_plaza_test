from rest_framework import serializers
from .models import Recipe, Step, Ingredient
from django.contrib.auth.models import User


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient


class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = IngredientSerializer(many=True)
    steps = StepSerializer(many=True)

    class Meta:
        model = Recipe

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient['name'])
            recipe.ingredients.add(ingredient)
        return recipe

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
             setattr(instance, key, value)
        instance.save()

    def delete(self, instance):
        instance.delete()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    recipes = RecipeSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = User


