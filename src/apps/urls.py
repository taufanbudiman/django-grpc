from django.urls.conf import path, include
from src.apps.users.views import UserSSOLoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

urlpatterns = [
    path('api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/logout', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/login/sso', UserSSOLoginView.as_view(), name='token_sso'),
    path('api/users', include('src.apps.users.urls'))
]