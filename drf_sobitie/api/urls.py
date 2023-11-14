from django.urls import include, path
from rest_framework.routers import DefaultRouter

from drf_sobitie.api.views import (
    CheckForSubscription,
    EventViewSet,
    NotificationsViewSet,
    QuestionQuizViewSet,
    QuestionViewSet,
    QuizResultViewSet,
    QuizViewSet,
    QuoteViewSet,
    StickerpackViewSet,
    VKView,
)

router = DefaultRouter()

router.register("events", EventViewSet, basename="events")
router.register("notifications", NotificationsViewSet, basename="notifications")
router.register("quotes", QuoteViewSet, basename="quotes")
router.register(r"stickerpack", StickerpackViewSet, basename="stickerpack")
router.register("quizzes", QuizViewSet, basename="quizzes")
router.register("questions", QuestionViewSet, basename="questions")
router.register(r"quizzes/(?P<quiz_id>\d+)/quiz_result", QuizResultViewSet, basename="results")
router.register(r"quizzes/(?P<quiz_id>\d+)/quiz_questions", QuestionQuizViewSet, basename="results")

urlpatterns = [
    path("", include(router.urls)),
    path('vk/', VKView.as_view()),
    path("check_for_subscription/<int:user_id>/", CheckForSubscription.as_view()),
    path("vk/", VKView.as_view()),
]
