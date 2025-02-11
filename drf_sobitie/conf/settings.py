import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
NOTIFICATIONS_API_URL = os.getenv("NOTIFICATIONS_API_URL")
CHECK_FOR_SUBSCRIPTION_API_URL = os.getenv("CHECK_FOR_SUBSCRIPTION_API_URL")
API_ADDRESS = os.getenv("API_ADDRESS")
VK_APP_SERVICE_KEY=os.getenv("VK_APP_SERVICE_KEY")
VK_ACCESS_TOKEN = os.getenv("VK_ACCESS_TOKEN")
VK_GROUP_ID = int(os.getenv("VK_GROUP_ID"))

SECRET_KEY = os.getenv("DJ_SECRET_KEY", default="djangosecretkey_WG312t0k130fk13f")

DEBUG = os.getenv("DEBUG", default=False)

ALLOWED_HOSTS = ["*"]

if DEBUG is True:
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost",
    ]

SCHEDULER_CONFIG = {
    "apscheduler.jobstores.default": {
        "class": "django_apscheduler.jobstores:DjangoJobStore"
    },
    "apscheduler.executors.processpool": {"type": "threadpool"},
}


INSTALLED_APPS = [
    "channels",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "daphne",
    "django.contrib.staticfiles",
    "django_apscheduler",
    "rest_framework",
    "drf_sobitie.api.apps.ApiConfig",
    "drf_sobitie.event.apps.EventConfig",
    "drf_sobitie.sticker_pack.apps.StickersConfig",
    "drf_sobitie.bot.apps.BotConfig",
    "drf_sobitie.notifications.apps.NotificationsConfig",
    "drf_sobitie.vk_utils.apps.VkUtilsConfig"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "drf_sobitie.conf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "drf_sobitie.conf.asgi.application"
WSGI_APPLICATION = "drf_sobitie.conf.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db/db.sqlite3",
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = False


STATIC_URL = "static/"
MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CSRF_TRUSTED_ORIGINS = [
    "http://*.localhost",
    "http://localhost*",
    "http://*.127.0.0.1",
    "http://127.0.0.1*",
    "http://84.201.189.83",
    "http://51.250.93.9",
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://84.201.189.83",
    "http://51.250.93.9"
]
