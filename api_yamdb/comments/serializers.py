from rest_framework import serializers

from .models import CommentModel, ReviewModel


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewModel
        fields = '__all__'
        read_only_fields = ('pub_date', 'author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'review')
        model = CommentModel
        read_only = ('author', 'review')
