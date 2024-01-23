from rest_framework import serializers

from titles.models import CategoriesModel, GenresModel


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор для категорий произведений."""
    class Meta:
        model=CategoriesModel
        fields = ['name', 'slug', ]


class GenresSerializer(serializers.ModelSerializer):
    """Сериализатор для жанров произведений."""
    class Meta:
        model=GenresModel
        fields = ['name', 'slug', ]