from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from users.models import UserConfirm
from users.serializers import RegisterSerializer, ConfirmSerializer, LoginSerializer
import random


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data, is_active=False)
        confirm = UserConfirm.objects.create(user=user, code=random.randint(10000, 99999))
        return Response({'user': 'created', "code": confirm.code, "data": serializer.data},
                        status=status.HTTP_201_CREATED)


class ConfirmAPIView(CreateAPIView):
    serializer_class = ConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get("code")
        confirm = get_object_or_404(UserConfirm, code=code)
        user = confirm.user
        user.is_active = True
        user.save()
        confirm.delete()
        return Response({"status": "user activated"}, status=status.HTTP_200_OK)

    class LoginAPIView(APIView):
        serializer_class = LoginSerializer

        def post(self, request, *args, **kwargs):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = authenticate(**serializer.validated_data)
            login(request, user)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                user.save()
                return Response({"token": token.key})
            return Response({"error invalide": "неправильные данные"}, status=status.HTTP_400_BAD_REQUEST)