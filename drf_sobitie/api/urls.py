from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, EventViewSet, QuoteViewSet

router = DefaultRouter()

router.register("categories", CategoryViewSet, basename="categories")
router.register("events", EventViewSet, basename="events")
router.register("quotes", QuoteViewSet, basename="quotes")

urlpatterns = [
    path("", include(router.urls)),
]
