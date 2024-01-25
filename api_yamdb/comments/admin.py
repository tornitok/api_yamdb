from comments.models import CommentModel, ReviewModel
from django.contrib import admin


class ReviewInline(admin.TabularInline):
    verbose_name = 'Комментарии к отзыву'
    verbose_name_plural = 'Комментарии к отзыву'
    model = CommentModel
    extra = 1
    max_num = 5
    classes = ['collapse ', 'extrapretty']


@admin.register(ReviewModel)
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


@admin.register(CommentModel)
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
