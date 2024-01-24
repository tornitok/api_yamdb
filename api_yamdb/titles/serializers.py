from rest_framework import serializers

from titles.models import CategoriesModel, GenresModel, TitlesModel


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор для категорий произведений."""

    class Meta:

        model = CategoriesModel
        fields = ['name', 'slug', ]


class GenresSerializer(serializers.ModelSerializer):
    """Сериализатор для жанров произведений."""

    class Meta:
        model = GenresModel
        fields = ['name', 'slug', ]


class TitlesSerializer(serializers.ModelSerializer):
    """Сериализатор для произведений."""

    genre = GenresSerializer(required=False, many=True)

    class Meta:
        model = TitlesModel
        fields = ['name', 'description', 'year', 'genre', 'category']

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
