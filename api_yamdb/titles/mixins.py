from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from users.permissions import IsAdminOrReadOnly


class BaseCategoriesGenresMixin(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
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
    lookup_field = 'slug'
