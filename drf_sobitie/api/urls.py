from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, EventViewSet, QuestionViewSet, QuizViewSet, QuizResultViewSet, QuoteViewSet

router = DefaultRouter()

router.register("categories", CategoryViewSet, basename="categories")
router.register("events", EventViewSet, basename="events")
router.register("quotes", QuoteViewSet, basename="quotes")
router.register("quizzes", QuizViewSet, basename="quizzes")
router.register("questions", QuestionViewSet, basename="questions")
router.register(r"quizzes/(?P<quiz_id>\d+)/results", QuizResultViewSet,
                basename="results")
router.register(r"quizzes/(?P<quiz_id>\d+)/questions", QuizViewSet,
                basename="results")

urlpatterns = [
    path("", include(router.urls)),
]
