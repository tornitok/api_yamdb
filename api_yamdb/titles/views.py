from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from titles.models import CategoriesModel
from titles.serializers import CategoriesSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """Представление для категорий произведений"""

    queryset = CategoriesModel.object.all()
    ordering = [
        'name',
    ]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        'name',
    ]
    serializer_class = CategoriesSerializer
