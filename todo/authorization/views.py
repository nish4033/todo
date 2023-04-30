from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.authorization.serializers import LoginSerializer, UserSerializer


class RegisterUser(APIView):
    authentication_classes = []

    def post(self, request):
        ser = UserSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        data = {
            "message": f"User created successfully. for '{user.email}' "
            f"please login."
        }
        return Response(data, status=status.HTTP_201_CREATED)


class LoginUser(APIView):
    authentication_classes = []

    def post(self, request):
        ser = LoginSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.validated_data
        return Response(data, status=status.HTTP_201_CREATED)
