import re
from datetime import datetime
import requests
import vk_api
from dotenv import load_dotenv
import os

load_dotenv()
from vk_api.bot_longpoll import VkBotLongPoll

VK_SERVICE_KEY = os.getenv("VK_SERVICE_KEY")

def longpoll_vk(): 
    vk_session = vk_api.VkApi(token=VK_SERVICE_KEY)
    longpoll = VkBotLongPoll(vk_session, group_id=215478360)
    for event in longpoll.listen():
        data=event.obj
        requests.post('http://127.0.0.1:8000/api/vk/', data=dict(data))

if __name__ == '__main__':
    longpoll_vk()
