import requests
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from account.api import UserSerializer
from .models import Problem, Submission, Language, Solution, WeeklyProblemSelection

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ["id", "source", "problem_id", "rating", "name", "tags", "coin_value"]


class ProblemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    ordering_fields = ("rating")
    
    @action(detail=True, methods=["GET"])
    def get_statement(self, request, pk=None):
        if not pk:
            return Response("No problem ID in request.", status=400)
        try:
            p = Problem.objects.get(id=pk)
            res = requests.get(p.link())
            if res.status_code != 200:
                return Response("Failed to retrieve")
        except:
            return Response("Problem ID given is invalid.", status=400)
        return Response(res)

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

class WeeklyProblemSelectionSerializer(serializers.ModelSerializer):

    problem_list = ProblemSerializer(many=True)
    class Meta:
        model = WeeklyProblemSelection
        fields = ["id", "problem_list", "week_start", "week_end"]
        depth = 1

class WeeklyProblemSelectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeeklyProblemSelection.objects.all()
    serializer_class = WeeklyProblemSelectionSerializer

    @action(detail=False, methods=["GET"])
    def get_user_weeklies(self, request, pk=None):
        uid = request.GET.get("user_id")
        if not uid:
            return Response("No user ID in request.", status=400)
        try:
            uid = int(uid)
            u = User.objects.get(id=uid)
        except:
            return Response("User ID given is invalid.", status=400)
        obj = WeeklyProblemSelection.get_for_date(u, datetime.now().date())
        serializer = WeeklyProblemSelectionSerializer(obj, many=False)
        return Response(serializer.data)