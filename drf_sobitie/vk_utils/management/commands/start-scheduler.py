import logging

from django.core.management.base import BaseCommand

from conf.settings import FORMAT
from drf_sobitie.vk_utils.scheduler import scheduler


class Command(BaseCommand):
    help = "Start scheduler."

    def handle(self, *args, **options):
        try:
            logging.basicConfig(
                format=FORMAT,
                level=logging.INFO,
                handlers=[logging.StreamHandler()],
            )
            scheduler.start()
        except Exception:
            logging.basicConfig(
                format=FORMAT,
                level=logging.INFO,
                handlers=[logging.StreamHandler()],
            )
            scheduler.shutdown()
