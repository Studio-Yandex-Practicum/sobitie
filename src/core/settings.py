from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_LEVEL = "INFO"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
