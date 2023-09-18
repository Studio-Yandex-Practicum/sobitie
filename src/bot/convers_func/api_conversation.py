import httpx

from core import settings


class APIClient:
    def __init__(self, host: str = None):
        self._host = host
        self._httpx_client = httpx.AsyncClient(base_url=self._host)

    async def get_events(self):
        async with self._httpx_client as session:
            return await session.get("/api/events/")

    async def get_quote(self):
        async with self._httpx_client as session:
            return await session.get("/api/quotes/")

    async def get_stickers(self):
        async with self._httpx_client as session:
            return await session.get("/api/stickerpack/")

    async def get_quizes_request(self):
        async with self._httpx_client as session:
            return await session.get(f"{self._host}/api/quizzes/")

    async def get_question(self, current_quiz_id, params):
        async with self._httpx_client as session:
            questions_url = f"{self._host}/api/quizzes/{current_quiz_id}/quiz_questions/"
            return await session.get(questions_url, params=params)

    async def get_message(self, current_quiz_id, params):
        async with self._httpx_client as session:
            message_url = f"{self._host}/api/quizzes/{current_quiz_id}/quiz_result/"
            return await session.get(message_url, params=params)

    async def send_notification(self, user_id):
        async with self._httpx_client as session:
            return await session.post(url="/api/notifications/", data={"user_id": user_id})

    async def unsubscribe_and_notify(self, user_id):
        async with self._httpx_client as session:
            return await session.delete(url=f"/api/notifications/{user_id}/")

    async def get_notify_event(self):
        async with self._httpx_client as session:
            return await session.get("/api/notifications/")

    async def block_error(self, user_id):
        async with self._httpx_client as session:
            return await session.delete(url=f"/api/notifications/{user_id}/")

    async def get_create_notification(self, user_id):
        async with self._httpx_client as session:
            return await session.get(url=f"/api/check_for_subscription/{user_id}/")


def get_client():
    return APIClient(settings.HOST)
