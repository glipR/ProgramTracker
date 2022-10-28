from django.db.models.signals import post_save
from django.dispatch import receiver
from problems.models import Submission
from streaks.models import StreakDay

@receiver(post_save, sender=Submission)
def create_streak_on_save(sender, instance: Submission, **kwargs):
    if StreakDay.objects.filter(user=instance.user, streak_day=instance.submission_time.date().isoformat()).count() == 0:
        StreakDay.objects.create(
            user=instance.user,
            streak_day=instance.submission_time.date().isoformat(),
            is_freeze=False,
            submission_source=instance,
        )
