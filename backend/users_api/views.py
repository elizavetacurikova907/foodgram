from djoser.views import UserViewSet as DefaultUserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Subscribe
from .serializers import SubscribeSerializer


class UserViewSet(DefaultUserViewSet):

    def get_permissions(self):
        if self.action in ('subscriptions', 'subscribe'):
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ('subscribe', 'subscriptions'):
            return SubscribeSerializer
        return super().get_serializer_class()

    @action(
        detail=False,
        methods=['get'],
        url_path='subscriptions',
    )
    def subscriptions(self, request):
        """Список авторов, на которых подписан текущий пользователь."""
        queryset = Subscribe.objects.filter(
            follower=request.user
        ).select_related('author')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=['post', 'delete'],
        url_path='subscribe',
    )
    def subscribe(self, request, pk=None):
        """Подписка/отписка на автора по его id."""
        author = self.get_object()
        user = request.user
        if request.method == 'POST':
            if author == user:
                return Response(
                    {'errors': 'Нельзя подписаться на себя'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if Subscribe.objects.filter(follower=user, author=author).exists():
                return Response(
                    {'errors': 'Вы уже подписаны на этого автора'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer = self.get_serializer(
                data=request.data,
                context={**self.get_serializer_context(), 'author_id': pk}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        Subscribe.objects.filter(follower=user, author=author).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
