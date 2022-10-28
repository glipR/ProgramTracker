from django.contrib import admin
from .models import StreakDay

@admin.register(StreakDay)
class StreakAdmin(admin.ModelAdmin):
    ordering = ("-streak_day", )
