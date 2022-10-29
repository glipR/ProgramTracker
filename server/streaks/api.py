from rest_framework import serializers, viewsets
from .models import StreakDay

class StreakDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = StreakDay
        fields = ["user", "streak_day", "is_freeze", "submission_source"]


class StreakDayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StreakDay.objects.all()
    serializer_class = StreakDaySerializer
