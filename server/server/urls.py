from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from account.api import UserViewSet
from problems.api import ProblemViewSet, SubmissionViewSet, LanguageViewSet, WeeklyProblemSelectionViewSet
from streaks.api import StreakDayViewSet

from problems.views import problem

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"problems", ProblemViewSet)
router.register(r"submissions", SubmissionViewSet)
router.register(r"languages", LanguageViewSet)
router.register(r"streaks", StreakDayViewSet)
router.register(r"weeklies", WeeklyProblemSelectionViewSet)

urlpatterns = [
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('problems/<slug:problem_id>/', problem),
]
