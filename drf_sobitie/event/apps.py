from django.apps import AppConfig


class EventConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "drf_sobitie.event"
    verbose_name = "События"

    def ready(self):
        import drf_sobitie.event.signals  # noqa
