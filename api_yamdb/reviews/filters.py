import django_filters as filters

from .models import Title


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre__slug', method='filter_genre')
    category = filters.CharFilter(
        field_name='category__slug', lookup_expr='exact'
    )
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    year = filters.NumberFilter(field_name='year', lookup_expr='exact')

    class Meta:
        model = Title
        fields = ['genre', 'category', 'name', 'year']

    def __init__(self, *args, **kwargs):
        super(TitleFilter, self).__init__(*args, **kwargs)

    def filter_genre(self, queryset, name, value):
        lookup = '__'.join([name, 'exact'])
        return queryset.filter(**{lookup: value})
