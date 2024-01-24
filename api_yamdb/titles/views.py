from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from titles.mixins import BaseCategoriesGenresMixin
from titles.models import CategoriesModel, GenresModel, TitlesModel
from titles.serializers import CategoriesSerializer, GenresSerializer, TitlesSerializer
from users.permissions import IsAdminOrReadOnly


class CategoriesViewSet(BaseCategoriesGenresMixin):
    """Представление для категорий произведений"""

    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer


class GenresViewSet(BaseCategoriesGenresMixin):
    """Представление для жанров произведений"""

    queryset = GenresModel.objects.all()
    serializer_class = GenresSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    """Представление для сотрудников."""

    queryset = TitlesModel.objects.all().select_related("category")
    permission_classes = [IsAdminOrReadOnly, ]
    filterset_fields = [
        "category__slug",
        "genre__slug",
        "name",
        "year",
    ]
    ordering = [
        "name",
    ]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    serializer_class = TitlesSerializer
