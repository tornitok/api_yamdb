from django.contrib import admin
from titles.models import CategoriesModel, GenresModel, TitlesModel


class TitlesInline(admin.TabularInline):
    verbose_name = 'Жанры произведения'
    verbose_name_plural = 'Жанры произведения'
    model = TitlesModel.genre.through
    extra = 1
    max_num = 5
    classes = ['collapse ', 'extrapretty']


@admin.register(TitlesModel)
class TitlesAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'category',
        'year',
    ]
    list_display = [
        'name',
        'category',
        'year',
    ]
    list_display_links = [
        'category',
    ]
    ordering = [
        'name',
    ]
    list_filter = [
        'category',
        'genre',
        'year',
    ]
    inlines = [
        TitlesInline,
    ]


@admin.register(CategoriesModel)
class CategoriesModelAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'slug',
    ]
    list_display = [
        'name',
        'slug',
    ]
    ordering = [
        'name',
    ]


@admin.register(GenresModel)
class GenresModelAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'slug',
    ]
    list_display = [
        'name',
        'slug',
    ]
    ordering = [
        'name',
    ]
