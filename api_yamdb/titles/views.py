from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, response, viewsets
from titles.mixins import BaseCategoriesGenresMixin
from titles.models import CategoriesModel, GenresModel, TitlesModel
from titles.serializers import (
    CategoriesSerializer,
    GenresSerializer,
    TitlesCreateUpdateSerializer,
    TitlesDetailSerializer,
)
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

    queryset = TitlesModel.objects.all().select_related('category')
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    filterset_fields = [
        'category__slug',
        'genre__slug',
        'name',
        'year',
    ]
    ordering = [
        'name',
    ]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TitlesDetailSerializer
        return TitlesCreateUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = TitlesCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance_serializer = TitlesDetailSerializer(instance)
        return response.Response(instance_serializer.data)
