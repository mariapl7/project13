from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели товара."""

    class Meta:
        model = Product
        fields = '__all__'


class CommentSerializer:
    pass