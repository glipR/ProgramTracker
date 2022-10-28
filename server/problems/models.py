from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    
    PROBLEM_SOURCES = (
        ("CF", "CodeForces"),
    )
    
    source = models.CharField(choices=PROBLEM_SOURCES, max_length=4)
    problem_id = models.CharField(max_length=255)
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
    submission_id = models.CharField(max_length=50)
    
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
