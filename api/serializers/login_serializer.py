from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68, min_length=8, write_only=True,
                                     style={'input_type': 'password'}, trim_whitespace=True)
    