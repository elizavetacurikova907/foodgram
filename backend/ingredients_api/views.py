from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Ingredient
from .serializers import IngredientSoloSerializer


class IngredientViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSoloSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'head', 'options']
