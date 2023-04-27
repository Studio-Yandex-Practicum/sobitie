from django.db import models


class Stickerpack(models.Model):
    name = models.CharField(
        max_length=50, unique=True, blank=False,
        verbose_name="Название стикерпака",
        help_text="введите название стикерпака"
    )
    image = models.ImageField(
        upload_to="images/", null=True,
        blank=True, verbose_name="Превью"
    )
    description = models.TextField(
        verbose_name="Описание стикер-пака",
        blank=True, help_text="Опишите стикерпак"
    )
    url_sticker = models.URLField(
        unique=True, verbose_name="Ссылка на стикер-пак",
        blank=False, help_text="Вставьте ссылку на стикерпак"
    )
    is_active = models.BooleanField(default=False, verbose_name="Активно")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Стикер-пак"
        verbose_name_plural = "Стикер-паки"
        db_table = "Stickerpack"
