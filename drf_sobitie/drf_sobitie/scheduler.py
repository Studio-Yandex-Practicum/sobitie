import vk_api
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_job
from vk_api.tools import VkTools

from api.views import VKView

from drf_sobitie.settings import VK_SERVICE_KEY, VK_GROUP_ID

scheduler = BackgroundScheduler()

vk_session = vk_api.VkApi(token=VK_SERVICE_KEY)
tools = VkTools(vk_session)


def remove_not_actual_events(events, vk_posts):
    for event in events:
        if event.vk_post_id not in [post["id"] for post in vk_posts["items"]]:
            event.delete()


@register_job(scheduler, "interval", seconds=10)
def check_vk_group_news_job():
    vk_posts = tools.get_all("wall.get", 1, {"owner_id": -VK_GROUP_ID})
    vk_view = VKView()
    vk_view.remove_not_actual_events(vk_posts)
    vk_view.update_events(vk_posts)


try:
    check_vk_group_news_job()
    scheduler.start()
except Exception:
    scheduler.shutdown()
