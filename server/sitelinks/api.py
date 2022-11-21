from re import S
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User

from .models import CodeForcesLink

class CFLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeForcesLink
        fields = ["id", "user", "handle", "last_created_submission_time", "last_created_submission_id"]


class CFLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CodeForcesLink.objects.all()
    serializer_class = CFLinkSerializer

    permission_classes = []

    @action(detail=False, methods=["POST"])
    def add_submissions(self, request, pk=None):
        try:
            user_id = request.data["user_id"]
            user = User.objects.get(id=user_id)
        except:
            return Response("Be sure to provide a valid user id at the top level of your post request.", status=400)
        try:
            submissions = request.data["submissions"]
        except:
            return Response("Please post an object with 'user_id' and 'submisisons'", status=400)
        try:
            CFLink:CodeForcesLink = self.get_queryset().get(user=user)
        except:
            return Response("Logged in user has no CFLink set up.", status=400)
#        try:
        CFLink.add_new_cf_submissions(submissions)
#        except:
#            return Response("Failed to add submissions", status=500)
        return Response("Complete", status=200)
