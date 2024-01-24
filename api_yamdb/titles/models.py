from django.core.validators import RegexValidator
from django.db import models


class CategoriesModel(models.Model):
    """Категории (типы) произведений."""

    name = models.CharField('Наименование категории', max_length=256)
    slug = models.SlugField(
        'Slug',
        max_length=50,
        unique=True,
        validators = [
            RegexValidator(regex='^[-a-zA-Z0-9_]+$')
        ]
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class GenresModel(models.Model):
    """Категории жанров."""

    name = models.CharField('Наименование жанра', max_length=256)
    slug = models.SlugField(
        'Slug',
        max_length=50,
        unique=True,
        validators = [
            RegexValidator(regex='^[-a-zA-Z0-9_]+$')
        ]
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class TitlesModel(models.Model):
    """Произведения, к которым пишут отзывы
    (oпределённый фильм, книга или песенка)."""

    name = models.TextField('Наименование произведения', max_length=256)
    category = models.ForeignKey(
        CategoriesModel,
        verbose_name='Категория произведения',
        on_delete=models.RESTRICT,
    )
    genre = models.ManyToManyField(
        GenresModel, verbose_name='Жанры произведения', related_name='genres'
    )
    year = models.IntegerField('Год создания произведения')
    description = models.TextField(
        'Описание произведения',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
