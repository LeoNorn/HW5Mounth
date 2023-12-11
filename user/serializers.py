from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import UserConfirm


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_fields = {
            "password": {"write_only": True}
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3)
    password = serializers.CharField(min_length=8)


class ConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfirm
        fields = ['code']
