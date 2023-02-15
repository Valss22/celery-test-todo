from django.contrib.auth.backends import ModelBackend

from .models import UserProfile


class EmailOrPhoneNumberBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user_profile = UserProfile.objects.get(email=username)
        except UserProfile.DoesNotExist:
            try:
                user_profile = UserProfile.objects.get(phone_number=username)
            except UserProfile.DoesNotExist:
                return None
        if user_profile.user.check_password(password):
            return user_profile
