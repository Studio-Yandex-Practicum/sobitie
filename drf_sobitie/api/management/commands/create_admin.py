import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create SuperUser if it doesn't exist yet"

    def handle(self, *args, **kwargs):
        logging.basicConfig(
            format=settings.FORMAT,
            level=logging.INFO,
            handlers=[logging.StreamHandler()],
        )

        if not User.objects.filter(is_superuser=True).exists():
            new_user = User(username='admin', is_superuser=True, is_staff=True)
            new_user.set_password('admin')
            new_user.save()
