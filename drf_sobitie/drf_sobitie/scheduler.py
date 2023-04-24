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
    for event in events:
        if event not in [post["id"] for post in vk_posts["items"]]:
            event.delete()


@register_job(scheduler, "interval", minutes=15)
def task():
    """Обновление записей в бд при их изменении в ВК (а также при их удалении),
    работает через планировщик. В параметре minutes указывается через сколько
    произойдет проверка обновлений на стене сообщества.
    """
    events = Event.objects.order_by("-event_time")
    vk_posts = tools.get_all("wall.get", 1, {"owner_id": -215478360})
    remove_not_actual_events(events, vk_posts)

    for post in vk_posts["items"]:
        post_id = post["id"]
        if events.filter(pk=post_id).exists():
            event = events.get(pk=post_id)
            event_date = event.event_time
            current_date = datetime.now()
            if event_date < current_date:
                break
            text = event["text"].split("#")[0].rstrip()

            if text == event.description:
                continue
            VKView().put(event, event["id"])
        else:
            text = post["text"]
            request_data = {
                "text": text,
                "id": post_id
            }
            requests.post("http://localhost:8000/api/vk/", data=request_data)


try:
    scheduler.start()
except Exception:
    scheduler.shutdown()
