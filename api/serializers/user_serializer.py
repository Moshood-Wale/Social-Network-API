from rest_framework import serializers
from models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fullname', 'ip_address', 'is_admin', 'created_at', 'updated_at']
