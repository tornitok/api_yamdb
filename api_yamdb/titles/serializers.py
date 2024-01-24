from django.db.models import Sum
from rest_framework import serializers

from titles.models import CategoriesModel, GenresModel, TitlesModel


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор для категорий произведений."""

    class Meta:
        model = CategoriesModel
        fields = [
            'name',
            'slug',
        ]
        lookup_field = 'slug'


class GenresSerializer(serializers.ModelSerializer):
    """Сериализатор для жанров произведений."""

    class Meta:
        model = GenresModel
        fields = [
            'name',
            'slug',
        ]
        lookup_field = 'slug'


class TitlesDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для подробностей о произведений."""

    category = CategoriesSerializer()
    genre = GenresSerializer(
        many=True,
    )
    rating = serializers.SerializerMethodField()

    class Meta:
        model = TitlesModel
        fields = '__all__'

    def get_rating(self, obj):
        return TitlesModel.reviews.annotate(total=Sum('score')) or 0


class TitlesCreateUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для подробностей о произведений."""

    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=CategoriesModel.objects.all(),
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=GenresModel.objects.all(),
        many=True,
    )

    class Meta:
        model = TitlesModel
        fields = '__all__'