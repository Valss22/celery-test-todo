from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib import admin
from django.urls import path

from apps.user.views import user_login, user_logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", user_login),
    path("api/logout/", user_logout),
    path("api/password-reset/", PasswordResetView.as_view()),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view()),
]
