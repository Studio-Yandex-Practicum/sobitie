import os
from datetime import datetime

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


@register_job(scheduler, "interval", minutes=1)
def task():
    """Обновление записей в бд при их изменении в ВК (а также при их удалении),
    работает через планировщик. В параметре minutes указывается через сколько
    произойдет проверка обновлений на стене сообщества.
    """
    events_db = Event.objects.all().filter(event_time__gte=datetime.now())
    list_vk_post_id = [event.vk_post_id for event in events_db]

    for event in tools.get_all_iter("wall.get", 100, {"owner_id": -215478360}):
        try:
            if Event.objects.get(vk_post_id=event["id"]).event_time.replace(
                hour=0, minute=0, second=0, microsecond=0, tzinfo=None
            ) < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
                break
            event_db = Event.objects.get(vk_post_id=event["id"])
            text = event["text"].split("#")[0].rstrip()
            if text == event_db.description:
                spent = list_vk_post_id.index(event_db.vk_post_id)
                list_vk_post_id.pop(spent)
                continue
            VKView().put(event, event["id"])
            spent = list_vk_post_id.index(event_db.vk_post_id)
            list_vk_post_id.pop(spent)
        except Event.DoesNotExist:
            if len(list_vk_post_id) != 0:
                for vk_post_id in list_vk_post_id:
                    event_db = Event.objects.get(vk_post_id=vk_post_id)
                    event_db.delete()


try:
    scheduler.start()
except Exception:
    scheduler.shutdown()
