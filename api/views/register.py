from rest_framework import generics, permissions, status
from api.serializers.register_serializer import RegisterSerializer
from api.lib.response import Response
from api.models.user import User


class RegisterUserView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        email = user_data.get('email', '')
        fullname = user_data.get('fullname', '')
        password = user_data.get('password', '')

        serializer.is_valid(raise_exception=True)
        user = User.objects.create(fullname=fullname, email=email, password=password)
        user.set_password(password)

        user.save()

        return Response(data=dict(serializer.data), status=status.HTTP_201_CREATED)
