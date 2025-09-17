from rest_framework import serializers
from .models import Product, Comment


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели товара."""

    class Meta:
        model = Product
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели комментария."""

    class Meta:
        model = Comment
        fields = '__all__'
