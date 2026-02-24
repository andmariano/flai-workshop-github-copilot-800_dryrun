"""
URL configuration for octofit_tracker project.
"""
import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    api_root,
    UserViewSet,
    TeamViewSet,
    ActivityViewSet,
    LeaderboardEntryViewSet,
    WorkoutViewSet,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Use the DRF `api_root` view from `views.py` which is properly
    # decorated and returns Codespaces-aware absolute URLs.
    path('', api_root, name='api-root'),
    path('api/', api_root, name='api-root-prefix'),
    path('api/', include(router.urls)),
]

