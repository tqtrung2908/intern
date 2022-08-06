from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from user.API.serializers import UserSerializers, RegisterSerializer, LoginSerializers


class UserView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.all()
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializers(user, many=True)
        return Response(serializer.data)


class LoginView(APIView):
    serializer_class = LoginSerializers

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
