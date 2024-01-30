from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Categories, Comment, Genres, Review, Title

User = get_user_model()


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор для категорий произведений."""

    class Meta:
        model = Categories
        fields = [
            'name',
            'slug',
        ]
        lookup_field = 'slug'


class GenresSerializer(serializers.ModelSerializer):
    """Сериализатор для жанров произведений."""

    class Meta:
        model = Genres
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
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'


class TitlesCreateUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для подробностей о произведений."""

    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all(),
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        many=True,
    )

    class Meta:
        model = Title
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )
    title_id = serializers.PrimaryKeyRelatedField(
        queryset=Title.objects.all(),
        source='title',
    )

    class Meta:
        model = Review
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = (
            'pub_date',
            'author',
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'review_id')
        model = Comment
