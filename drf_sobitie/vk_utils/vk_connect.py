import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll

from drf_sobitie.conf.settings import (
    VK_GROUP_ID, VK_ACCESS_TOKEN, API_ADDRESS
)


def longpoll_vk():
    vk_session = vk_api.VkApi(token=VK_ACCESS_TOKEN)
    longpoll = VkBotLongPoll(vk_session, group_id=VK_GROUP_ID)
    for event in longpoll.listen():
        data = event.obj
        requests.post(f"{API_ADDRESS}/api/vk/", data=dict(data))


if __name__ == "__main__":
    longpoll_vk()
