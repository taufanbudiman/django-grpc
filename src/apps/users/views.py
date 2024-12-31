from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from src.apps.users.serializers import UserSerializer, CustomUserLoginSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class UserListView(ListAPIView):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.model.objects.all()

class UserProtectedListView(ListAPIView):
    model = User
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.all()

class UserSSOLoginView(TokenObtainPairView):
    serializer_class = CustomUserLoginSerializer