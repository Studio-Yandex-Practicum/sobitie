import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll

from drf_sobitie.drf_sobitie.settings import VK_USER_KEY, VK_GROUP_ID


def longpoll_vk():
    vk_session = vk_api.VkApi(token=VK_USER_KEY)
    longpoll = VkBotLongPoll(vk_session, group_id=VK_GROUP_ID)
    for event in longpoll.listen():
        data = event.obj
        requests.post("http://127.0.0.1:8000/api/vk/", data=dict(data))


if __name__ == "__main__":
    longpoll_vk()
