from rest_framework import filters, mixins, viewsets
from users.permissions import (
    IsAdminOrModeratorOrReadOnly,
    isNotUserRole,
    isNotModeratorRole,
)


class BaseCategoriesGenresMixin(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
):
    permission_classes = [
        isNotUserRole,
        isNotModeratorRole,
        IsAdminOrModeratorOrReadOnly,
    ]
    ordering = [
        'name',
    ]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        'name',
    ]
    lookup_field = 'slug'
