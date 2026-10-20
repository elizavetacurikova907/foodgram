from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.db import models

from constants import (
    EMAIL_MAX_LENGTH,
    USERNAME_MAX_LENGTH,
)


class User(AbstractUser):
    username = models.CharField(
        'Имя пользователя',
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': 'Пользователь с таким именем уже существует.',
        },
    )
    email = models.EmailField(
        unique=True,
        max_length=EMAIL_MAX_LENGTH,
        verbose_name='Адрес электронной почты',
        error_messages={
            'unique': 'Пользователь с таким email уже существует.',
        },
    )
    first_name = models.CharField(
        'Имя',
        max_length=USERNAME_MAX_LENGTH,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=USERNAME_MAX_LENGTH,
        blank=True
    )

    def clean(self):
        super().clean()
        if self.username == 'me':
            raise ValidationError('Использовать имя me запрещено!')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def create_superuser(
        self, username, email=None, password=None, **extra_fields
    ):
        self.clean(username)
        return super().create_superuser(
            username, email, password, **extra_fields
        )

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_superuser or self.is_staff

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username
