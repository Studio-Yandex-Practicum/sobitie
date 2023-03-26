import re
from datetime import datetime

import vk_api
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_job
from vk_api.tools import VkTools
from api.views import VKView
from event.models import Event
from dotenv import load_dotenv
import os

load_dotenv()
scheduler = BackgroundScheduler()

VK_LOGIN = os.getenv("VK_LOGIN")
VK_PASSWORD = os.getenv("VK_LOGIN")
login, password = VK_LOGIN, VK_PASSWORD
vk_session = vk_api.VkApi(login, password)
vk_session.auth(token_only=True)
tools=VkTools(vk_session)

@register_job(scheduler, 'interval', seconds=10)
def task():
    "Обновление записей в бд при их изменении в ВК"
    for event in tools.get_all_iter('wall.get', 100, {'owner_id': -215478360}):
        try:
            if Event.objects.get(vk_post_id=event['id']).event_time.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
                break
            event_db=Event.objects.get(vk_post_id=event['id']).description
            if event['text']==event_db:
                continue
            VKView().put(event, event['id'])
        except Event.DoesNotExist:
            pass           
            

try:
    scheduler.start()
except Exception as e:
    print(e)
    scheduler.shutdown()
