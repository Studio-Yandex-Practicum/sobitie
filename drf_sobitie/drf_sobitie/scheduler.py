import os
from datetime import datetime

import requests
import vk_api
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_job
from dotenv import load_dotenv
from vk_api.tools import VkTools

from api.views import VKView
from event.models import Event

load_dotenv()
scheduler = BackgroundScheduler()

VK_SERVICE_KEY = os.getenv("VK_SERVICE_KEY")
vk_session = vk_api.VkApi(token=VK_SERVICE_KEY)
tools = VkTools(vk_session)


def remove_not_actual_events(events, vk_posts):
    """Удаление записей в бд при их удалении в сообществе ВК."""
    for event in events:
        event_vk_post_id = event.vk_post_id
        if event_vk_post_id not in [post["id"] for post in vk_posts["items"]]:
            event.delete()


@register_job(scheduler, "interval", seconds=10)
def task():
    """Обновление записей в бд при их изменении в ВК (а также при их удалении),
    работает через планировщик. В параметре seconds указывается через сколько
    секунд произойдет проверка обновлений на стене сообщества.
    """
    events = Event.objects.order_by("-event_time")
    vk_posts = tools.get_all("wall.get", 1, {"owner_id": -217419974})
    remove_not_actual_events(events, vk_posts)

    for post in vk_posts["items"]:
        request_data = {
                "text": post["text"],
                "id": post["id"]
            }
        if not events.filter(vk_post_id=post["id"]).exists():
            requests.post("http://localhost:8000/api/vk/", data=request_data)
        else:
            event = events.get(vk_post_id=post["id"])
            event_date = event.event_time
            current_date = datetime.now()
            post_text = post["text"].split("#")[0].rstrip()
            if not (event_date < current_date) and (post_text != event.description):
                VKView().put(request_data, post["id"])
            continue

try:
    scheduler.start()
except Exception:
    scheduler.shutdown()
