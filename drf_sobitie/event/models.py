from django.db import models


class Category(models.Model):
    name = models.CharField(
        'Название категории',
        unique=True,
        max_length=256,
    )
    add_time = models.DateTimeField('Дата добавления', auto_now_add=True)
    change_time = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(
        'Название категории',
        unique=True,
        max_length=256,
    )
    description = models.TextField(
        'Подробное описание',
        blank=True,
        null=True,
    )
    add_time = models.DateTimeField('Дата добавления', auto_now_add=True)
    change_time = models.DateTimeField('Дата изменения', auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='event'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=['name', 'description'],
                name='unique_event'
            ),
        )
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name
