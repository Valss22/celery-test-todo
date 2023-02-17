from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile


class EmailOrPhoneNumberBackend(ModelBackend):
    def authenticate(
        self,
        request,
        login,
        password,
    ):
        try:
            user_profile = UserProfile.objects.get(
                Q(email=login) | Q(phone_number=login)
            )
        except UserProfile.DoesNotExist:
            return None

        if user_profile.user.check_password(password):
            return user_profile.user
