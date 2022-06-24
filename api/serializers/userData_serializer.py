from rest_framework import serializers
from api.models.user_data import UserData


class UserDataSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = UserData
        fields = ('id', 'message', 'created_at', 'updated_at', 'client_ip')
        read_only_fields = ('date_created', 'client_ip')

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').META.get("REMOTE_ADDR")
        return UserData.objects.create(**validated_data)