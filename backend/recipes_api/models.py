from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from ingredients_api.models import Ingredient
from constants import NAME_MAX_LENGTH
from tags_api.models import Tag

User = get_user_model()

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        'Recipe', 
        on_delete=models.CASCADE, 
        related_name='recipe_ingredients',
    )
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        related_name='recipe_ingredients',
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
        default=1,
    )


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
        related_name='recipes',
    )
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        verbose_name='Название'
    )
    # image
    text = models.TextField(verbose_name='Описание')
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        related_name='recipes',
        through=RecipeIngredient,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        related_name='recipes',
    )
    cooking_time = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Время приготовления',
        default=30,
    )


class ShoppingListObject(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping_list_object',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='shopping_list_object',
    )


class FavoriteRecipes(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorite_object',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favorite_object',
    )
