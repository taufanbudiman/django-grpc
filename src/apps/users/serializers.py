from django.contrib.auth.models import User, update_last_login
from django.core.exceptions import ObjectDoesNotExist

from core.sso import validate_password_for_app
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django_socio_grpc import proto_serializers
from src.apps.users.grpc.users_pb2 import (
    UserListResponse,
    UserResponse
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        proto_class = UserResponse
        proto_class_list = UserListResponse

class CustomUserLoginSerializer(TokenObtainPairSerializer):
    app = serializers.CharField()

    def validate(self, attrs):
        try:
            user = User.objects.get(username=attrs['username'])
        except ObjectDoesNotExist:
            raise ValidationError('Username does not exist')

        # validate app password
        is_valid = validate_password_for_app(attrs['app'], attrs['password'], user.password)
        if not is_valid:
            raise ValidationError("username or password is incorrect")

        refresh = self.get_token(user)


        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, user)

        return {
            "access_token": str(refresh),
            "token_type": str(refresh.access_token),
        }