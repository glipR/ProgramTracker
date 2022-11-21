from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ["coins", "freezes", "rating"]


class UserSerializer(serializers.ModelSerializer):

    info = UserInfoSerializer(many=False)

    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff", "info", "codeforces"]
        depth = 1


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
