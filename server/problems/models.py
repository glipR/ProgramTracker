import datetime
import random
from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    
    PROBLEM_SOURCES = (
        ("CF", "CodeForces"),
    )
    
    source = models.CharField(choices=PROBLEM_SOURCES, max_length=4)
    problem_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    tags = models.JSONField(default=list)
    rating = models.IntegerField()
    
    @classmethod
    def get_problem_id(cls, source, other_info):
        if source == "CF":
            # ContestID/ProblemIndex
            return f"{other_info[0]}/{other_info[1]}"
        return ""

    def get_short_source_name(self):
        if self.source == "CF":
            return "CF"
        return "??"

    def coin_value(self):
        return (self.rating - 200) // 50

    def __str__(self):
        return f"{self.get_short_source_name()}-{self.problem_id}"

class Language(models.Model):
    
    show_name = models.CharField(max_length=50)
    file_extension = models.CharField(max_length=10)
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.show_name

class Submission(models.Model):
    """
    A submission is just a judge submission on the respective site.
    """
    
    problem = models.ForeignKey(Problem, related_name="submissions", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_id = models.CharField(max_length=50)
    submission_time = models.DateTimeField(default=datetime.datetime.now())
    
    result = models.CharField(max_length=48)
    time_taken = models.IntegerField()
    memory_taken = models.IntegerField()

class Solution(models.Model):
    """
    A solution is something that is maintained for every user/problem pairing.
    It can be made public / private, and receive upvotes.
    """
    
    problem = models.ForeignKey(Problem, related_name="solutions", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    code = models.TextField()
    whiteboard_data = models.TextField()
    explanation = models.TextField()

class WeeklyProblemSelection(models.Model):
    """
    A set of problems which when solved give the user bonus coins and a streak freeze.
    Resets weekly. Problems are selected in order to push a bit above the users current rating.
    """

    user = models.ForeignKey(User, related_name="weeklies", on_delete=models.CASCADE)
    problem_list = models.ManyToManyField(Problem)
    week_start = models.DateField()
    week_end = models.DateField()
    
    @classmethod
    def create_from_date(cls, user: User, date: datetime.date):
        start_date = date - datetime.timedelta(days=(date.isoweekday() - 1))
        end_date = start_date + datetime.timedelta(days=7)
        problems = cls.generate_problems_for(user)
        obj = WeeklyProblemSelection.objects.create(
            user=user,
            week_start=start_date,
            week_end=end_date,
        )
        obj.problem_list.set(problems)
        return obj
    
    @classmethod
    def get_for_date(cls, user: User, date: datetime.date):
        return WeeklyProblemSelection.objects.filter(user=user, week_start__lte=date, week_end__gt=date)

    @classmethod
    def generate_problems_for(self, user: User):
        # Generate 3 problems the user has not solved, with a rating bound of (current user rating) to (current user rating + 400).
        possible_problems = list(Problem.objects.filter(rating__gte=user.info.rating(), rating__lte=user.info.rating()+400))
        possible_problems = [p for p in possible_problems if p.submissions.filter(user=user).count() == 0]
        random.shuffle(possible_problems)
        return possible_problems[:3]
