import time
import requests
import datetime
from django.db import models
from django.contrib.auth.models import User

from problems.models import Problem, Submission, Language

CF_NUM_SUBMISSIONS = 20

class CodeForcesLink(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="codeforces")
    handle = models.CharField(max_length=120)
    
    last_created_submission_time = models.BigIntegerField(default=-1)
    last_created_submission_id = models.BigIntegerField(default=-1)

    def __str__(self):
        return f"{self.user.username} - {self.handle}"

    def add_new_cf_submissions(self, submissions):
        for sub in submissions[::-1]:
            # Create relevant problem object if it does not exist.
            problem = sub["problem"]
            problem_id = Problem.get_problem_id("CF", [problem["contestId"], problem["index"]])
            if Problem.objects.get_queryset().filter(source="CF", problem_id=problem_id).count() == 0:
                p = Problem.objects.create(
                    source="CF",
                    problem_id=problem_id,
                    rating=problem.get("rating", 0),
                    name=problem["name"],
                    tags=problem["tags"],
                )
            else:
                p = Problem.objects.get(source="CF", problem_id=problem_id)
            if sub["verdict"] == "OK":
                # Create relevant submission object.
                sub_obj, created = Submission.objects.get_or_create(
                    user=self.user,
                    submission_id=sub["id"],
                    submission_time=datetime.datetime.fromtimestamp(sub["creationTimeSeconds"]),
                    problem=p,
                    language=Language.objects.get_or_create(show_name=sub["programmingLanguage"])[0]
                )
                sub_obj.result = sub["verdict"]
                sub_obj.time_taken = sub["timeConsumedMillis"]
                sub_obj.memory_taken = sub["memoryConsumedBytes"]
                sub_obj.save()
        if len(submissions) > 0:
            self.last_created_submission_id = submissions[0]["id"]
            self.last_created_submission_time = submissions[0]["creationTimeSeconds"]
            self.save()
