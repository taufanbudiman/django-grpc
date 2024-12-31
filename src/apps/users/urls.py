from django.urls.conf import path

from src.apps.users.views import (
    UserListView,
    UserProtectedListView
)

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('/protected', UserProtectedListView.as_view(), name='user_list_protected'),
]