from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CheckForSubscription,
    EventViewSet,
    NotificationsViewSet,
    QuestionViewSet,
    QuizResultViewSet,
    QuizViewSet,
    QuoteViewSet,
    VKView,
)

router = DefaultRouter()

router.register("events", EventViewSet, basename="events")
router.register("notifications", NotificationsViewSet, basename="notifications")
router.register("quotes", QuoteViewSet, basename="quotes")
router.register("quizzes", QuizViewSet, basename="quizzes")
router.register("questions", QuestionViewSet, basename="questions")
router.register(r"quizzes/(?P<quiz_id>\d+)/results", QuizResultViewSet, basename="results")
router.register(r"quizzes/(?P<quiz_id>\d+)/questions", QuizViewSet, basename="results")


urlpatterns = [
    path("", include(router.urls)),
    path("check_for_subscription/<int:user_id>/", CheckForSubscription.as_view()),
    path("vk/", VKView.as_view()),
]
