import logging

from django.core.management.base import BaseCommand

from django.conf import settings
from drf_sobitie.vk_utils.vk_connect import longpoll_vk


class Command(BaseCommand):
    help = "Start scheduler."

    def handle(self, *args, **options):
        logging.basicConfig(
            format=settings.FORMAT,
            level=logging.INFO,
            handlers=[logging.StreamHandler()],
        )
        logging.info('START SCHEDULER')
        longpoll_vk()

