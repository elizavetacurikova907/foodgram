from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken

from .models import User

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email', 'username', 'first_name',
            'last_name', 'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ListRetriveUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email', 'id', 'username', 'first_name',
            'last_name', 'is_subscribed', 'avatar',
        )


# class TokenSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, attrs):
#         user = authenticate(username=attrs['email'], password=attrs['password'])
#         if user is None:
#             raise serializers.ValidationError(
#                 {'detail': 'Неверный логин или пароль'}
#             )
#         attrs['user'] = user
#         return attrs

#     def create(self, validated_data):
#         user = validated_data['user']
#         token = AccessToken.for_user(user)
#         return {'auth_token': str(token)}
