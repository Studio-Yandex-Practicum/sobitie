import logging
import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll

from django.conf import settings
log = logging.getLogger(__name__)
 
def longpoll_vk():
    vk_session = vk_api.VkApi(token=settings.VK_ACCESS_TOKEN)
    longpoll = VkBotLongPoll(vk_session, group_id=settings.VK_GROUP_ID)
    for event in longpoll.listen():
        data = event.obj
        resp = requests.post(f'http://{settings.API_ADDRESS}/api/vk/', data=dict(data))
        if resp.status_code != 200:
            log.error(f'unprocessed data: {data}')


if __name__ == "__main__":
    longpoll_vk()
