import time
import requests
from django.db import models
from django.contrib.auth.models import User

CF_NUM_SUBMISSIONS = 20

class CodeForcesLink(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="codeforces")
    handle = models.CharField(max_length=120)
    
    last_created_submission_time = models.BigIntegerField(default=-1)
    last_created_submission_id = models.BigIntegerField(default=-1)

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
        # TODO: Create relevant problem objects if they don't exist
        # TODO: Create relevant submission objects
        # These are different from solution objects.
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
