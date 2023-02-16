from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.user.views import (
    user_login,
    user_logout,
    password_reset,
    password_reset_confirm,
)
from apps.todo.views import TaskViewSet


router = routers.DefaultRouter()
router.register(r"todo", TaskViewSet, basename="todo")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/login/", user_login),
    path("api/logout/", user_logout),
    path("api/password-reset/", password_reset),
    path(
        "api/password-reset-confirm/<uidb64>/<token>/",
        password_reset_confirm,
        name="password_reset_confirm",
    ),
]
