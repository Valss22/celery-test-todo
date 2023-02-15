from django.contrib import admin
from django.urls import path

from apps.user.views import user_login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/login/", user_login),
]
