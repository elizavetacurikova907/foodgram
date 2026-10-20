from django.db import models

from constants import TAG_NAME_MAX_LENGTH, TAG_SLUG_MAX_LENGTH
from validators import slug_regex


class Tag(models.Model):
    name = models.CharField(
        max_length=TAG_NAME_MAX_LENGTH,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=TAG_SLUG_MAX_LENGTH,
        unique=True,
        validators=[slug_regex],
        verbose_name='Слаг'
    )
