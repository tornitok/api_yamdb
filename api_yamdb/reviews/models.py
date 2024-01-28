from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models


User = get_user_model()


class Categories(models.Model):
    """Категории (типы) произведений."""

    name = models.CharField('Наименование категории', max_length=256)
    slug = models.SlugField(
        'Slug',
        max_length=50,
        unique=True,
        validators=[RegexValidator(regex='^[-a-zA-Z0-9_]+$')],
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genres(models.Model):
    """Категории жанров."""

    name = models.CharField('Наименование жанра', max_length=256)
    slug = models.SlugField(
        'Slug',
        max_length=50,
        unique=True,
        validators=[RegexValidator(regex='^[-a-zA-Z0-9_]+$')],
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Произведения, к которым пишут отзывы
    (oпределённый фильм, книга или песенка)."""

    name = models.TextField('Наименование произведения', max_length=256)
    category = models.ForeignKey(
        Categories,
        verbose_name='Категория произведения',
        on_delete=models.RESTRICT,
    )
    genre = models.ManyToManyField(
        Genres,
        verbose_name='Жанры произведения',
        related_name='titles',
        through='TitlesGenres',
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


class TitlesGenres(models.Model):
    """Промежуточная модель для Произведений-Жанров."""

    title = models.ForeignKey(
        Title, verbose_name='Произведение', on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genres, verbose_name='Жанр', on_delete=models.CASCADE
    )


class Review(models.Model):
    title_id = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField('Текст отзыва')
    author = models.ForeignKey(
        User,
        verbose_name='Автор отзыва',
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
    )
    score = models.IntegerField(
        'Рейтинг', validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ['author', 'title_id']

    def __str__(self):
        return self.title_id.name


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    review_id = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField('Текст комментария')
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
