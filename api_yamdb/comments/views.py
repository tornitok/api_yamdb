from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from titles.models import TitlesModel

from .models import CommentModel, ReviewModel
from users.permissions import IsAuthorAdminModerOrReadOnly
from .serializers import CommentSerializer, ReviewSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorAdminModerOrReadOnly, ]

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        new_queryset = CommentModel.objects.filter(review__id=review_id)
        return new_queryset

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        post = get_object_or_404(ReviewModel, id=review_id)
        serializer.save(author=self.request.user, post=post)


class ReviewModelViewSet(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorAdminModerOrReadOnly, ]

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        post = get_object_or_404(TitlesModel, id=title_id)
        serializer.save(author=self.request.user, post=post)
