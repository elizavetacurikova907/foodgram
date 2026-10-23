from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Subscribe(models.Model):
    # author - на кого подписан пользователь
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Создатель контента',
        related_name='subscribers',
    )
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='subscriptions',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'follower'],
                name='unique_author_follower'
            )
        ]
