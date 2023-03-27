from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, CheckForSubscription, EventViewSet, NotificationsView, QuoteViewSet

router = DefaultRouter()

router.register("categories", CategoryViewSet, basename="categories")
router.register("events", EventViewSet, basename="events")
router.register("quotes", QuoteViewSet, basename="quotes")

urlpatterns = [
    path("", include(router.urls)),
    path("notifications/", NotificationsView.as_view()),
    path("check_for_subscription/<int:user_id>/", CheckForSubscription.as_view()),
]
