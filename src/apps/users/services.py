from django.contrib.auth.models import User
from django_socio_grpc import generics

from src.apps.users.serializers import UserProtoSerializer


class UserService(generics.AsyncReadOnlyModelService):
    queryset = User.objects.all()
    serializer_class = UserProtoSerializer