from django.contrib import admin

from event.models import Event, Category

admin.site.register(Event)
admin.site.register(Category)
