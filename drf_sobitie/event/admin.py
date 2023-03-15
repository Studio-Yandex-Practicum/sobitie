from django.contrib import admin
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

from event.models import Category, Event, Quote

LENGTH_OF_QUOTE_DISPLAY = 200


class QuoteAdmin(admin.ModelAdmin):
    date_hierarchy = "add_time"
    list_display = (
        "id",
        "short_text",
        "author",
        "thumbnail_of_image",
        "add_time",
    )
    list_display_links = ("id", "short_text")
    search_fields = ("text", "author")
    empty_value_display = "-пусто-"

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
        return truncatechars(obj.text, LENGTH_OF_QUOTE_DISPLAY)


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = "event_time"
    list_display = (
        "id",
        "name",
        "location",
        "event_time",
        "category",
        "add_time",
        "change_time",
    )
    list_display_links = ("id", "name")
    search_fields = ("name", "location")
    list_filter = ("category",)
    empty_value_display = "-пусто-"


class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = "add_time"
    list_display = ("id", "name", "add_time", "change_time")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    empty_value_display = "-пусто-"


admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Quote, QuoteAdmin)
