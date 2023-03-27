import asyncio
from functools import partial

import requests


async def async_get_request(url: str) -> requests.Response:
    """Отправляет GET-запрос по URL."""
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(None, requests.get, url)
    return response


async def async_send_json_post_request(url: str, data: dict) -> requests.Response:
    """Отправляет POST-запрос по URL с json в теле."""
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(None, partial(requests.post, url, json=data))
    return response


async def async_delete_request(url: str) -> requests.Response:
    """Отправляет DELETE-запрос по URL."""
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(None, requests.delete, url)
    return response
