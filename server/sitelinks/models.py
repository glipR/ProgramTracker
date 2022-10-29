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

    def get_new_submissions(self):
        previous_time = self.last_created_submission_time
        previous_id = self.last_created_submission_id
        submissions = []
        start = 1
        at_end = False
        all_submissions = []
        while not at_end:
            # Get 10 at a time.
            request_url = f"https://codeforces.com/api/user.status?handle={self.handle}&from={start}&count={CF_NUM_SUBMISSIONS}"
            res = requests.get(request_url)
            if res.status_code != 200:
                time.sleep(2)
                continue
            submissions = res.json()["result"]
            if len(submissions) == 0:
                at_end = True
            for sub in submissions:
                if previous_time > sub["creationTimeSeconds"] or previous_id == sub["id"]:
                    at_end = True
                    break
                all_submissions.append(sub)
            start += len(submissions)
        if len(all_submissions) > 0:
            self.last_created_submission_id = all_submissions[0]["id"]
            self.last_created_submission_time = all_submissions[0]["creationTimeSeconds"]
            self.save()
        for sub in all_submissions:
            # Create relevant problem object if it does not exist.
            problem = sub["problem"]
            problem_id = Problem.get_problem_id("CF", [problem["contestId"], problem["index"]])
            if Problem.objects.get_queryset().filter(source="CF", problem_id=problem_id).count() == 0:
                p = Problem.objects.create(
                    source="CF",
                    problem_id=problem_id,
                    rating=problem["rating"],
                    name=problem["name"],
                    tags=problem["tags"],
                )
            else:
                p = Problem.objects.get(source="CF", problem_id=problem_id)
            if sub["verdict"] == "OK":
                # Create relevant submission object.
                Submission.objects.create(
                    user=self.user,
                    submission_id=sub["id"],
                    problem=p,
                    result=sub["verdict"],
                    language=Language.objects.get_or_create(show_name=sub["programmingLanguage"])[0],
                    submission_time=datetime.datetime.fromtimestamp(sub["creationTimeSeconds"]),
                    time_taken=sub["timeConsumedMillis"],
                    memory_taken=sub["memoryConsumedBytes"],
                )
        return all_submissions

def test_request():
    import requests
    res = requests.get("https://codeforces.com/api/user.status?handle=glipR&from=1&count=10")
    if res.status_code == 200:
        j = res.json()
        submissions = j["result"]
        first = submissions[0]
        first_id = first["id"]
        first_time = first["creationTimeSeconds"]
        problem_info = str(first["problem"]["contestId"]) + "/" + str(first["problem"]["index"])
        verdict = first["verdict"]
        timeConsumed = first["timeConsumedMillis"]
        memoryConsumed = first["memoryConsumedBytes"]
