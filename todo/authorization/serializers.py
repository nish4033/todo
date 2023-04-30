from django.conf import settings

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from todo.authorization.jwt import generate_jwt_token
from todo.authorization.password_haser import CustomPBKDF2PasswordHasher
from todo.operations.models import User
from todo.utils.custom_exception import PermissionDenied

hasher = CustomPBKDF2PasswordHasher()
salt = settings.SALT


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):  # noqa
        email = User.objects.filter(email=value)
        if email.exists():
            duplicate_obj = User.objects.get(email=email)
            raise ValidationError(
                {"details": f"user {duplicate_obj.user} already exists"}
            )
        return value

    def validate_password(self, val):
        password = val.encode("utf-8")
        hashed_password = hasher.encode(password, salt)

        return hashed_password

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        email = User.objects.filter(email=attrs["email"])

        if not email.exists():
            raise PermissionDenied(
                {"details": f"user {attrs['email']} doesn't exists"}
            )
        hashed_password = hasher.encode(attrs["password"], salt)
        user = User.objects.filter(
            email=attrs["email"], password=hashed_password
        ).values("id", "name", "email", "created")
        if not user.exists():
            raise PermissionDenied({"details": "Incorrect Password"})
        user = list(user)[0]
        token = generate_jwt_token(user)
        user.update({"token": token})
        return user
