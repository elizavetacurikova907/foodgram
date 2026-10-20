from django.db import models

from constants import (
    INGREDIENT_NAME_MAX_LENGTH,
    MEASUREMENT_CHOICES,
    MEASUREMENT_UNIT_MAX_LENGHT
)

class Ingredient(models.Model):
    name = models.CharField(
        max_length=INGREDIENT_NAME_MAX_LENGTH,
        unique=True,
        verbose_name='Название'
    )
    measurement_unit = models.CharField(
        max_length=MEASUREMENT_UNIT_MAX_LENGHT,
        choices=MEASUREMENT_CHOICES,
        verbose_name='Единица измерения'
    )
