from django.shortcuts import render
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .permissions import IsAdmin
from .serializers import (
    CreateUserSerializer,
    ListRetriveUserSerializer,
)


class UserViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
):
    queryset = User.objects.all()
    serializer_class = ListRetriveUserSerializer
    permission_classes = (AllowAny,)
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('username',)
    # http_method_names = ('get', 'post', 'patch', 'delete')

    def get_serializer_class(self):
        if self.action in ('create',):
            return CreateUserSerializer
        return ListRetriveUserSerializer

    @action(
        methods=('get',),
        detail=False,
        permission_classes=(IsAuthenticated,),
    )
    def me(self, request):
        serializer = ListRetriveUserSerializer(request.user)
        return Response(serializer.data)

    # def me_avatar(self, request):
    #     user = request.user
            
    #     # Обновление аватара (PUT/PATCH)
    #     if request.method in ('PUT', 'PATCH'):
    #         serializer = UserAvatarSerializer(user, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)
            
    #     # Удаление аватара (DELETE)
    #     elif request.method == 'DELETE':
    #         if user.avatar:
    #             user.avatar.delete(save=True)
    #         return Response(status=status.HTTP_204_NO_CONTENT)
