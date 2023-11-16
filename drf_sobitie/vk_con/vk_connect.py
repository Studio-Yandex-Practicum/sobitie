import requests
import vk_api
from django.conf import settings
from vk_api.bot_longpoll import VkBotLongPoll


def longpoll_vk():
    vk_session = vk_api.VkApi(token=settings.VK_SERVICE_KEY)
    longpoll = VkBotLongPoll(vk_session, group_id=settings.VK_GROUP_ID)
    for event in longpoll.listen():
        data = event.obj
        requests.post("http://127.0.0.1:8000/api/vk/", data=dict(data))


if __name__ == "__main__":
    longpoll_vk()
