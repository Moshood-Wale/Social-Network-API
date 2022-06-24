from rest_framework import generics
from rest_framework import status
from api.serializers.login_serializer import LoginSerializer
from django.contrib.auth import authenticate
from api.lib.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email", "")
        password = request.data.get("password", "")

        if email is None or password is None:
            return Response(
                errors={
                    "invalid_credentials": "Please provide both email and password"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(email=email, password=password)

        if not user:
            return Response(
                errors={
                    "invalid_credentials": "Ensure both email and password are correct"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.is_active:
            return Response(
                errors={"invalid_credentials": "Your account has been deactivated"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        token = RefreshToken.for_user(user).access_token
        return Response(
            data={"user_id": user.id, "token": str(token)}, status=status.HTTP_200_OK
        )
