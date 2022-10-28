from django.db import models
from django.contrib.auth.models import User

from problems.models import Submission

class StreakDay(models.Model):
    
    user = models.ForeignKey(User, related_name="streak_days", on_delete=models.CASCADE)
    streak_day = models.DateField()
    is_freeze = models.BooleanField()
    submission_source = models.ForeignKey(Submission, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user.username} - {self.streak_day.isoformat()}"
