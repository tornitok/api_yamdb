from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Roles(models.TextChoices):
        USER = 'user', 'Пользователь'
        MODERATOR = 'moderator', 'Модератор'
        ADMIN = 'admin', 'Админ'

    role = models.CharField(
        max_length=12,
        choices=Roles.choices,
        default=Roles.USER,
        null=True,
    )
    bio = models.TextField(
        max_length=150,
        blank=True,
        null=True,
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
    )
    confirmation_code = models.CharField(
        verbose_name='Код авторизации',
        max_length=6,
        blank=True,
        null=True
    )
