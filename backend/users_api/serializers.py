from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from djoser.serializers import UserSerializer as DefaultUserSerializer
from rest_framework import serializers

from .models import Subscribe
from recipes_api.models import Recipe
from recipes_api.serializers import ShortRecipeSerializer

User = get_user_model()

class CustomUserSerializer(DefaultUserSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta(DefaultUserSerializer.Meta):
        model = User
        fields = (*DefaultUserSerializer.Meta.fields, 'is_subscribed')

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Subscribe.objects.filter(
                user=request.user,
                author=obj
            ).exists()
        return False


class SubscribeUserSerializer(CustomUserSerializer):
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta(DefaultUserSerializer.Meta):
        model = User
        fields = (
            *CustomUserSerializer.Meta.fields,
            'recipes',
            'recipes_count',
        )

    def get_recipes_count(self, obj):
        recipes = Recipe.objects.filter(author=obj)
        recipes_count = len(recipes)
        return recipes_count

    def get_recipes(self, obj):
        recipes = Recipe.objects.filter(author=obj)[:3]
        return ShortRecipeSerializer(
            recipes,
            many=True,
            context=self.context
        ).data


class SubscribeSerializer(serializers.ModelSerialiser):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Subscribe
        fields = ()

    def create(self, validated_data):
        follower = self.context.get('request').user
        author_id = self.context.get('author_id')
        author = get_object_or_404(User, id=author_id)
        subscribe = Subscribe.objects.create(
            author=author,
            follower=follower
        )
        return subscribe

    def to_representation(self, instance):
        return SubscribeUserSerializer(
            instance.author, 
            context=self.context
        ).data


# class CreateDeleteSerializer(serializers.ModelSerialiser):

#     class Meta:
#         model = Subscribe
#         fields = ('author')

#     def create(self, validated_data):
#         follower = self.context.get('request').user
#         subscribe = Subscribe.objects.create(
#             **validated_data,
#             follower=follower
#         )
#         return subscribe
