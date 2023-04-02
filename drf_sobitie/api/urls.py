from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CheckForSubscription,
    EventViewSet,
    NotificationsViewSet,
    QuoteViewSet,
    VKView,
)

router = DefaultRouter()

router.register("events", EventViewSet, basename="events")
router.register("quotes", QuoteViewSet, basename="quotes")
router.register("notifications", NotificationsViewSet, basename="notifications")

urlpatterns = [
    path("", include(router.urls)),
    path("vk/", VKView.as_view()),
    path("check_for_subscription/<int:user_id>/", CheckForSubscription.as_view()),
]
