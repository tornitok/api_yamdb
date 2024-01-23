from rest_framework import serializers

from titles.models import CategoriesModel


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор для категорий произведений."""
    class Meta:
        model=CategoriesModel
        fields = "__all__"
    