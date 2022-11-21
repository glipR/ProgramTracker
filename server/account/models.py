from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="info")
    coins = models.IntegerField(default=0)
    freezes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Info"

    def rating(self):
        from problems.models import Submission

        # TODO: Better rating.
        s = Submission.objects.filter(user=self.user).order_by("-submission_time")[:30]
        submissions = list(s)
        contribution = 1
        cur_contributing = len(submissions)
        rating_sum = 800
        for sub in submissions:
            contribution += cur_contributing
            rating_sum += cur_contributing * sub.problem.rating
            cur_contributing -= 1
        return rating_sum // contribution
