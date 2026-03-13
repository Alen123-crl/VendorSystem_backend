from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        min_length=3,
        max_length=255,
        required=True,
        error_messages={
            "required": "Username is required",
            "min_length": "Username must be at least 3 characters",
            "max_length": "Username cannot exceed 255 characters"
        }
    )

    password = serializers.CharField(
        write_only=True,
        min_length=6,
        max_length=25,
        required=True,
        error_messages={
            "required": "Password is required",
            "min_length": "Password must be at least 6 characters",
            "max_length": "Password cannot exceed 25 characters"
        }
    )

    class Meta:
        model = User
        fields = ["username", "password"]

    def validate_username(self, value):

        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Username already exists"
            )

        return value

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )

        return user
  
class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(
        min_length=3,
        max_length=255,
        required=True
    )

    password = serializers.CharField(
        write_only=True,
        min_length=6,
        max_length=25,
        required=True
    )

    def validate(self, data):

        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError(
                "Invalid username or password"
            )

        refresh = RefreshToken.for_user(user)

        return {
            "user_id": user.id,
            "username": user.username,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        }