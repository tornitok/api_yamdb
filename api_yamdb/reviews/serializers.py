from datetime import datetime

from django.contrib.auth import get_user_model
from django.db.models import Avg
from rest_framework import serializers

from .models import Categories, Genres, Title, Comment, Review


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
    rating = serializers.SerializerMethodField(source='score')

    class Meta:
        model = Title
        fields = '__all__'

    def get_rating(self, obj):
        score = obj.reviews.aggregate(total=Avg('score')) or 0
        return score['total'] or None


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

    def validate_year(self, obj):
        current_datetime = datetime.now()
        if obj > current_datetime.year:
            raise serializers.ValidationError(
                'Год создания произведения не может быть больше текущего'
            )
        return obj


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )
    title_id = serializers.PrimaryKeyRelatedField(
        queryset=Title.objects.all()
    )
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = (
            'pub_date',
            'author',
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'review_id')
        model = Comment
        
