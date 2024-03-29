import datetime

from django.db import models


class Event(models.Model):
    description = models.TextField(
        "Подробное описание",
        blank=True,
        null=True,
    )
    add_time = models.DateTimeField("Дата добавления", auto_now_add=True)
    vk_post_id = models.IntegerField("Id поста в вк", blank=True, null=True)
    change_time = models.DateTimeField("Дата изменения", auto_now=True)
    event_time = models.DateTimeField("Дата события", default=datetime.datetime.today)
    location = models.CharField(
        "Место проведения",
        max_length=256,
        null=True,
        blank=True,
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=["description"], name="unique_event"),
        )
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return self.description[:200]


class Quote(models.Model):
    text = models.TextField(verbose_name="Текст цитаты")
    author = models.CharField(max_length=256, verbose_name="Автор цитаты")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    image = models.ImageField(
        upload_to="images/", null=True, blank=True, verbose_name="Изображение"
    )

    class Meta:
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"

    def __str__(self):
        return self.text[:120]


class Subscriber(models.Model):
    """Модель подписчика на уведомления о событиях."""

    user_id = models.BigIntegerField(verbose_name="id", unique=True, editable=False)
