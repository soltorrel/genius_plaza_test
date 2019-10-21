from django.urls import path, include
from .views import RecipesView, IngredientsView, StepsView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('recipes', RecipesView)
router.register('steps', StepsView)
router.register('ingredients', IngredientsView)


urlpatterns = [
    path('', include(router.urls))
]
