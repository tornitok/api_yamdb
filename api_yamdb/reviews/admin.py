from django.contrib import admin

from .models import Categories, Comment, Genres, Review, Title


class TitlesInline(admin.TabularInline):
    verbose_name = 'Жанры произведения'
    verbose_name_plural = 'Жанры произведения'
    model = Title.genre.through
    extra = 1
    max_num = 5
    classes = ['collapse ', 'extrapretty']


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
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


@admin.register(Categories)
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


@admin.register(Genres)
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


class ReviewInline(admin.TabularInline):
    verbose_name = 'Комментарии к отзыву'
    verbose_name_plural = 'Комментарии к отзыву'
    model = Comment
    extra = 1
    max_num = 5
    classes = ['collapse ', 'extrapretty']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    fields = [
        'author',
        'pub_date',
        'title_id',
        'text',
        'score',
    ]
    readonly_fields = [
        'pub_date',
    ]
    list_display = [
        'title_id',
        'text',
        'author',
        'pub_date',
    ]
    ordering = [
        'pub_date',
    ]
    list_filter = [
        'pub_date',
        'author',
        'score',
    ]
    inlines = [
        ReviewInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = [
        'pub_date',
        'author',
        'review_id',
        'text',
    ]
    readonly_fields = [
        'pub_date',
    ]
    list_display = [
        'review_id',
        'text',
        'author',
        'pub_date',
    ]
    ordering = [
        'pub_date',
    ]
    list_filter = [
        'review_id',
        'pub_date',
        'author',
    ]
