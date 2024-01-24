from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets

from users.permissions import IsAdminOrReadOnly


class BaseCategoriesGenresMixin(
    viewsets.GenericViewSet,
    generics.ListCreateAPIView,
    generics.DestroyAPIView,
):
    permission_classes = [IsAdminOrReadOnly]
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
