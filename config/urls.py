from django.contrib import admin
from django.urls import path

from apps.user.views import user_login, user_logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/login/", user_login),
    path("api/auth/logout/", user_logout),
]
