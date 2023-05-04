from django.contrib import admin
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

from .models import Stickerpack

LENGTH_OF_DESCRIPTION_DISPLAY = 50
EMPTY_VALUE = "-пусто-"


@admin.register(Stickerpack)
class StickerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "thumbnail_of_image",
        "is_active"
    )
    list_editable = ["is_active"]
    empty_value_display = EMPTY_VALUE

    @admin.display(description="Изображение")
    def thumbnail_of_image(self, obj):
        """Отображает в Админ-панели миниатюру изображения."""
        img_tag = self.empty_value_display
        if obj.image:
            img_tag = f'<img src="{obj.image.url}" style="max-height: 32px;">'
        return mark_safe(img_tag)

    @admin.display(description="Текст")
    def short_text(self, obj):
        """Укорачивает отображение цитаты в Админ-панели."""
        return truncatechars(obj.text, LENGTH_OF_DESCRIPTION_DISPLAY)
