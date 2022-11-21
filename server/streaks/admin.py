from django.contrib import admin
from .models import StreakDay


@admin.register(StreakDay)
class StreakAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "streak_day",
        "is_freeze",
        "submission_source",
        "streak_length",
    )
    ordering = ("-streak_day",)
