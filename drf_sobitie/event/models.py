import datetime

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
        'Название события',
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
    event_time = models.DateTimeField('Дата события', default=datetime.datetime.today)
    location = models.CharField(
        'Место проведения',
        max_length=256,
        null=True,
        blank=True,
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


class Quote(models.Model):
    text = models.TextField(
        verbose_name='Текст цитаты'
    )
    author = models.CharField(
        max_length=256,
        verbose_name='Автор цитаты'
    )
    add_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )
    image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    def __str__(self):
        return self.text[:120]
