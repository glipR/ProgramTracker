from rest_framework import serializers, viewsets

from account.api import UserSerializer
from .models import Problem, Submission, Language, Solution

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ["id", "source", "problem_id", "rating", "name", "tags"]


class ProblemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    ordering_fields = ("rating")

class SubmissionSerializer(serializers.ModelSerializer):
    
    problem = ProblemSerializer()
    user = UserSerializer()
    
    class Meta:
        model = Submission
        fields = [
            "id", 
            "problem", 
            "language", 
            "user",
            "submission_id",
            "submission_time",
            "result",
            "time_taken",
            "memory_taken",
        ]
        depth = 1
        

class SubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    ordering_fields = ("submission_time")

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["id", "show_name", "file_extension", "short_name"]


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
