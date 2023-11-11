import json

import requests
import vk_api
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_job
from vk_api.tools import VkTools


from drf_sobitie.settings import (
    VK_SERVICE_KEY, VK_GROUP_ID, API_ADDRESS
)


scheduler = BackgroundScheduler()

vk_session = vk_api.VkApi(token=VK_SERVICE_KEY)
tools = VkTools(vk_session)


@register_job(scheduler, "interval", seconds=10)
def check_vk_group_news_job():
    """Обновление записей в бд при их изменении в ВК (а также при их удалении),
    работает через планировщик. В параметре seconds указывается через сколько
    секунд произойдет проверка обновлений на стене сообщества.
    """
    vk_posts = tools.get_all("wall.get", 1, {"owner_id": -VK_GROUP_ID})
    requests.put(
        f"{API_ADDRESS}/api/vk/", data=json.dumps(vk_posts),
        headers={'Content-Type': 'application/json'}
    )


try:
    scheduler.start()
except Exception:
    scheduler.shutdown()
