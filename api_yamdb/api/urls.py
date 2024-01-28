from django.urls import include, path
from rest_framework import routers

from reviews.views import (
    CategoriesViewSet,
    CommentViewSet,
    GenresViewSet,
    ReviewModelViewSet,
    TitlesViewSet,
)

v1_router = routers.DefaultRouter()
v1_router.register(r'titles', TitlesViewSet)
v1_router.register(r'categories', CategoriesViewSet)
v1_router.register(r'genres', GenresViewSet)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='CommentModel',
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewModelViewSet,
    basename='ReviewModel',
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('', include('users.urls')),
]
