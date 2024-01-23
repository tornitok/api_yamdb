from titles.mixins import BaseCategoriesGenresMixin
from titles.models import CategoriesModel, GenresModel
from titles.serializers import CategoriesSerializer, GenresSerializer


class CategoriesViewSet(BaseCategoriesGenresMixin):
    """Представление для категорий произведений"""

    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer


class GenresViewSet(BaseCategoriesGenresMixin):
    """Представление для жанров произведений"""

    queryset = GenresModel.objects.all()
    serializer_class = GenresSerializer