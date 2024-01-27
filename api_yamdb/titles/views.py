from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework import permissions, response, viewsets, status

from titles.filters import TitleFilter
from titles.mixins import BaseCategoriesGenresMixin
from titles.models import CategoriesModel, GenresModel, TitlesModel
from titles.serializers import (
    CategoriesSerializer,
    GenresSerializer,
    TitlesCreateUpdateSerializer,
    TitlesDetailSerializer,
)
from users.permissions import (
    IsAdminOrModeratorOrReadOnly,
    isNotModeratorRole,
    isNotUserRole,
)


class CategoriesViewSet(BaseCategoriesGenresMixin):
    """Представление для категорий произведений"""

    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer


class GenresViewSet(BaseCategoriesGenresMixin):
    """Представление для жанров произведений"""

    queryset = GenresModel.objects.all()
    serializer_class = GenresSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    """Представление для произведений."""

    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = TitlesModel.objects.all()
    permission_classes = [
        isNotUserRole,
        isNotModeratorRole,
        IsAdminOrModeratorOrReadOnly,
    ]
    filterset_class = TitleFilter
    filter_backends = [
        filters.DjangoFilterBackend,
    ]
    ordering = [
        'name',
    ]
    filter_backends = [
        OrderingFilter,
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
        return response.Response(
            instance_serializer.data, status=status.HTTP_201_CREATED
        )