import os

import httpx
import requests

from core.settings import (
    CHECK_FOR_SUBSCRIPTION_API_URL,
    EVENTS_URL,
    NOTIFICATIONS_API_URL,
    QUIZZES_URL,
    QUOTE_URL,
    STICKERPACK_URL,
)


class APIClient:
    def __init__(self, host: str = None):
        self._host = os.getenv("HOST", "http://localhost:8000")
        self._httpx_client = httpx.AsyncClient(base_url="http://localhost:8000")  # Чтобы каждый раз не указывать хост в начале урла.

    async def get_events(self):
        async with self._httpx_client as session:
            return await session.get(EVENTS_URL)

    async def get_quote(self):
        async with self._httpx_client as session:
            return await session.get(QUOTE_URL)

    async def get_stickers(self):
        async with self._httpx_client as session:
            return await session.get(STICKERPACK_URL)

    def get_quizes_request(self):
        return requests.get(QUIZZES_URL)

    def get_question(self, current_quiz_id, params):
        questions_url = f"{QUIZZES_URL}{current_quiz_id}/quiz_questions/"
        return requests.get(questions_url, params=params)

    def get_message(self, current_quiz_id, params):
        message_url = f"{QUIZZES_URL}{current_quiz_id}/quiz_result/"
        return requests.get(message_url, params=params)

    async def send_notification(self, user_id):
        async with self._httpx_client as session:
            return await session.post(url=NOTIFICATIONS_API_URL, data={"user_id": user_id})

    async def unsubscribe_and_notify(self, user_id):
        async with self._httpx_client as session:
            return await session.delete(url=f"{NOTIFICATIONS_API_URL}{user_id}/")

    async def get_notify_event(self):
        async with self._httpx_client as session:
            return await session.get(NOTIFICATIONS_API_URL)

    async def block_error(self, user_id):
        async with self._httpx_client as session:
            return await session.delete(url=f"{NOTIFICATIONS_API_URL}{user_id}/")

    async def get_create_notification(self, user_id):
        async with self._httpx_client as session:
            return await session.get(url=f"{CHECK_FOR_SUBSCRIPTION_API_URL}{user_id}/")
