import json
import logging
import re
from datetime import datetime
from time import sleep

import requests
import vk_api
from apscheduler.schedulers import SchedulerNotRunningError
from apscheduler.schedulers.background import BackgroundScheduler

from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import register_job
from vk_api.tools import VkTools

from conf.settings import API_ADDRESS, VK_APP_SERVICE_KEY, VK_GROUP_ID, FORMAT

vk_session = vk_api.VkApi(token=VK_APP_SERVICE_KEY)
tools = VkTools(vk_session)


class PostsFilter:
    def __init__(self, posts):
        self.posts = posts

    @staticmethod
    def __get_event_time(post_text):
        event_time = re.search(r"\d\d\.\d\d\.\d{4} \d{2}:\d{2}", post_text).group(0)
        event_time = datetime.strptime(event_time, "%d.%m.%Y %H:%M")

        return event_time

    def __is_actual(self, post):
        return (
                "афиша события" in post["text"].lower()
                and self.__get_event_time(post["text"]) > datetime.now()
        )

    def filtering(self):
        return [post for post in self.posts if self.__is_actual(post)]


class Command(BaseCommand):
    help = "Start scheduler."

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()

        @register_job(scheduler, "interval", seconds=10)
        def check_vk_group_news_job():
            """Обновление записей в бд при их изменении в ВК (а также при их удалении),
            работает через планировщик. В параметре seconds указывается через сколько
            секунд произойдет проверка обновлений на стене сообщества.
            """
            vk_posts = tools.get_all("wall.get", 1, {"owner_id": -VK_GROUP_ID})
            requests.put(
                f"{API_ADDRESS}/api/vk/",
                data=json.dumps(PostsFilter(posts=vk_posts["items"]).filtering()),
                headers={'Content-Type': 'application/json'}
            )

        logging.basicConfig(
            format=FORMAT,
            level=logging.INFO,
            handlers=[logging.StreamHandler()],
        )
        scheduler.start()
        logging.basicConfig(
            format=FORMAT,
            level=logging.INFO,
            handlers=[logging.StreamHandler()],
        )

        while True:
            try:
                sleep(1)
            except (KeyboardInterrupt, SystemExit):
                logging.basicConfig(
                    format=FORMAT,
                    level=logging.INFO,
                    handlers=[logging.StreamHandler()],
                )
                scheduler.shutdown()
                logging.basicConfig(
                    format=FORMAT,
                    level=logging.INFO,
                    handlers=[logging.StreamHandler()],
                )
                break
            except SchedulerNotRunningError:
                scheduler = BackgroundScheduler()
                logging.basicConfig(
                    format=FORMAT,
                    level=logging.INFO,
                    handlers=[logging.StreamHandler()],
                )
                scheduler.start()
                logging.basicConfig(
                    format=FORMAT,
                    level=logging.INFO,
                    handlers=[logging.StreamHandler()],
                )
