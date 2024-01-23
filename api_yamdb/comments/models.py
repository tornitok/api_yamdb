from django.db import models
from titles.models import TitlesModel
from users.models import User


class Review(models.Model):
    title_id = models.ForeignKey(
        TitlesModel, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    score = models.IntegerField()


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    titles = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Rate(models.Model):
    titles = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
