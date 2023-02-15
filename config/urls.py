from django.contrib import admin
from django.urls import path

from apps.user.views import (
    user_login,
    user_logout,
    password_reset,
    password_reset_confirm,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", user_login),
    path("api/logout/", user_logout),
    path("api/password-reset/", password_reset),
    path(
        "api/password-reset-confirm/<user_id>/<token>/",
        password_reset_confirm,
        name="password_reset_confirm",
    ),
]
