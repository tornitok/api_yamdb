from django.urls import include, path
from rest_framework import routers

from titles.views import CategoriesViewSet, GenresViewSet, TitlesViewSet
from comments.views import CommentViewSet, ReviewModelViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'titles', TitlesViewSet)
v1_router.register(r'categories', CategoriesViewSet)
v1_router.register(r'genres', GenresViewSet)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewModelViewSet)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
