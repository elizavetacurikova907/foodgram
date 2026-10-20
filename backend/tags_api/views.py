from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Tag
from .serializers import TagSerializer


class TagViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'head', 'options']
