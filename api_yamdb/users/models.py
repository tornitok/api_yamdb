from django.contrib.auth.models import AbstractUser
from django.db import models

from core.constants import (MAX_LENGTH_CODE_USERS, MAX_LENGTH_USERS,
                            MAX_LENGTH_USERS_ROLE)


class User(AbstractUser):
    class Roles(models.TextChoices):
        USER = 'user', 'Пользователь'
        MODERATOR = 'moderator', 'Модератор'
        ADMIN = 'admin', 'Админ'

    role = models.CharField(
        max_length=MAX_LENGTH_USERS_ROLE,
        choices=Roles.choices,
        default=Roles.USER,
        null=True,
    )
    bio = models.TextField(
        max_length=MAX_LENGTH_USERS,
        blank=True,
        null=True,
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=MAX_LENGTH_USERS,
        unique=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
    )
    confirmation_code = models.CharField(
        verbose_name='Код авторизации',
        max_length=MAX_LENGTH_CODE_USERS,
        blank=True,
        null=True
    )

    @property
    def is_user(self):
        return self.role == self.Roles.USER

    @property
    def is_moderator(self):
        return self.role == self.Roles.MODERATOR
