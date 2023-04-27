import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_LEVEL = "INFO"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
EVENTS_URL = os.getenv("EVENTS_URL")
QUOTE_URL = os.getenv("QUOTE_URL")
STICKERPACK_URL = os.getenv("STICKERPACK_URL")
QUIZZES_URL = os.getenv("QUIZZES_URL")
NOTIFICATIONS_API_URL = os.getenv("NOTIFICATIONS_API_URL")
CHECK_FOR_SUBSCRIPTION_API_URL = os.getenv("CHECK_FOR_SUBSCRIPTION_API_URL")
