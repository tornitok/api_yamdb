from django_filters import rest_framework as filters

from titles.models import TitlesModel


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre__slug', lookup_expr='exact')
    category = filters.CharFilter(
        field_name='category__slug', lookup_expr='exact'
    )
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    year = filters.NumberFilter(field_name='year', lookup_expr='exact')

    class Meta:
        model = TitlesModel
        fields = ['genre', 'category', 'name', 'year']
