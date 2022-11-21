import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from problems.models import Submission, WeeklyProblemSelection
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

@receiver(post_save, sender=Submission)
def give_coins_and_freeze_on_completion(sender, instance: Submission, **kwargs):
    coins = instance.problem.coin_value()
    info = instance.user.info
    info.coins += coins
    weekly = WeeklyProblemSelection.get_for_date(instance.user, datetime.datetime.now().date())
    if weekly.problem_list.contains(instance.problem):
        info.freezes += 1
    info.save()
