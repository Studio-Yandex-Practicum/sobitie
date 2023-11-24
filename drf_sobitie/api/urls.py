from django.urls import include, path
from rest_framework.routers import DefaultRouter

from drf_sobitie.api.views import (
    CheckForSubscription,
    EventViewSet,
    NotificationsViewSet,
    QuoteViewSet,
    StickerpackViewSet,
    VKView,
)
from drf_sobitie.notifications.views import send_event_notification

router = DefaultRouter()

router.register("events", EventViewSet, basename="events")
router.register("notifications", NotificationsViewSet, basename="notifications")
router.register("quotes", QuoteViewSet, basename="quotes")
router.register(r"stickerpack", StickerpackViewSet, basename="stickerpack")

urlpatterns = [
    path("", include(router.urls)),
    path("vk/", VKView.as_view()),
    path("check_for_subscription/<int:user_id>/", CheckForSubscription.as_view()),
    path("send-event-notification/", send_event_notification, name="send_event_notification"),
    path("vk/", VKView.as_view()),
]
