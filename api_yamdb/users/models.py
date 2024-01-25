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
    )
    bio = models.TextField()

    if role == 'moderator' or role == 'admin':
        is_staff = True
        is_superuser = True
