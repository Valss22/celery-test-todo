from django.contrib.auth.backends import ModelBackend

from .models import UserProfile


class EmailOrPhoneNumberBackend(ModelBackend):
    def authenticate(
        self,
        request,
        login,
        password,
    ):
        try:
            user_profile = UserProfile.objects.get(email=login)
        except UserProfile.DoesNotExist:
            try:
                user_profile = UserProfile.objects.get(phone_number=login)
            except UserProfile.DoesNotExist:
                return None

        if user_profile.user.check_password(password):
            return user_profile.user
