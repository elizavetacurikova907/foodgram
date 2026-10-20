from rest_framework import serializers

from .models import Ingredient

class IngredientSoloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')
