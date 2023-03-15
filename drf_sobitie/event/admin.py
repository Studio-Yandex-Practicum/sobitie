from django.contrib import admin

from event.models import Category, Event, Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ("text", "author", "image", "add_time")
    search_fields = ("text", "author")
    list_filter = ("add_time",)
    empty_value_display = "-пусто-"


admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Quote, QuoteAdmin)
