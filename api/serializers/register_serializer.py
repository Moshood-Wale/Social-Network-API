from rest_framework import serializers
from api.models.user import User
import re 


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True,
                                     style={'input_type': 'password'}, trim_whitespace=True)
    
    class Meta:
        model = User
        fields = ['email', 'fullname', 'password']

    def validate_fullname(self, fullname):
        regex = re.compile(r'^[a-zA-Z\s]+$')
        if regex.match(fullname):
            return fullname
        raise serializers.ValidationError("Enter a valid fullname")

    def validate_email(self, email):
        regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        if regex.match(email):
            return email
        raise serializers.ValidationError("Enter a valid email address")

    def save(self):
        user = User(
            fullname=self.validated_data["fullname"],
            email=self.validated_data["email"],
            phone_number=self.validated_data["phone_number"],
        )
        user.set_password(self.validated_data["password"])
        user.save()
        return user
