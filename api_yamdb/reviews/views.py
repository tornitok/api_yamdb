from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import permissions, response, status, viewsets
from rest_framework.filters import OrderingFilter

from users.permissions import (
    IsAdminOrModeratorOrReadOnly,
    IsAuthorOrAdminOrModeratorOrReadOnly,
    isNotModeratorRole,
    isNotUserRole,
)

from .filters import TitleFilter
from .mixins import BaseCategoriesGenresMixin
from .models import Categories, Comment, Genres, Review, Title
from .serializers import (
    CategoriesSerializer,
    CommentSerializer,
    GenresSerializer,
    ReviewSerializer,
    TitlesCreateUpdateSerializer,
    TitlesDetailSerializer,
)

User = get_user_model()


class CategoriesViewSet(BaseCategoriesGenresMixin):
    """Представление для категорий произведений"""

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class GenresViewSet(BaseCategoriesGenresMixin):
    """Представление для жанров произведений"""

    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    """Представление для произведений."""

    http_method_names = ['get', 'post', 'patch', 'delete']

    queryset = Title.objects.all()

    permission_classes = [
        isNotUserRole,
        isNotModeratorRole,
        IsAdminOrModeratorOrReadOnly,
    ]

    filterset_class = TitleFilter
    ordering = [
        'name',
    ]
    filter_backends = [
        OrderingFilter,
    ]

    def filter_queryset(self, queryset):
        filter_backends = (filters.DjangoFilterBackend,)

        for backend in list(filter_backends):
            queryset = backend().filter_queryset(
                self.request, queryset, view=self
            )
        return queryset

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


class CommentViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthorOrAdminOrModeratorOrReadOnly,
    ]

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        new_queryset = Comment.objects.filter(review_id=review_id)
        return new_queryset

    def create(self, request, *args, **kwargs):
        review_id = kwargs.get('review_id')
        get_object_or_404(Review, pk=review_id)
        data = request.data.dict()
        data['author'] = request.user
        data['review_id'] = review_id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED
        )


class ReviewModelViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        IsAuthorOrAdminOrModeratorOrReadOnly,
    ]

    def create(self, request, *args, **kwargs):
        title_id = kwargs.get('title_id')
        get_object_or_404(Title, pk=title_id)
        data = request.data.dict()
        data['author'] = request.user
        data['title_id'] = title_id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED
        )
