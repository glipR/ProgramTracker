from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StreakDay

# TODO: Achievements on instance.streak_length() hitting certain thresholds.
