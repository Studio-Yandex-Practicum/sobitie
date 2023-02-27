from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, EventViewSet

router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('events', EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls)),
]
