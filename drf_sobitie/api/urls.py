from api.views import EventViewSet, QuoteViewSet, VKView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("events", EventViewSet, basename="events")
router.register("quotes", QuoteViewSet, basename="quotes")

urlpatterns = [
    path("", include(router.urls)),
    path("vk/", VKView.as_view()),
]
