import json
import re
from datetime import datetime

import requests
import vk_api
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_job
from vk_api.tools import VkTools


from drf_sobitie.drf_sobitie.settings import (
    VK_SERVICE_KEY, VK_GROUP_ID, API_ADDRESS
)


scheduler = BackgroundScheduler()

vk_session = vk_api.VkApi(token=VK_SERVICE_KEY)
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


try:
    scheduler.start()
except Exception:
    scheduler.shutdown()
