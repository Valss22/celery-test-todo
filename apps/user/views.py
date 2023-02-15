from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from config.settings import EMAIL_HOST


@api_view(["POST"])
def user_login(request: Request):
    email = request.data.get("email")
    phone_number = request.data.get("phone_number")
    password = request.data["password"]

    user = authenticate(
        request, login=email if email else phone_number, password=password
    )
    if user is not None:
        login(request, user)
        return Response(
            {"message": "Authentication successful"},
            status=status.HTTP_200_OK,
        )
    return Response(
        {"message": "Invalid credentials"},
        status=status.HTTP_401_UNAUTHORIZED,
    )


@api_view(["POST"])
def user_logout(request: Request):
    logout(request)
    return Response(
        {"message": "Logged out successfully"},
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def password_reset(request: Request):
    email = request.data.get("email")
    if email:
        try:
            user = User.objects.get(profile__email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "No user found with that email address"},
                status=status.HTTP_404_NOT_FOUND,
            )
        uidb64 = urlsafe_base64_encode(str(user.pk).encode())
        token = default_token_generator.make_token(user)
        reset_url = reverse(
            "password_reset_confirm", kwargs={"uidb64": uidb64, "token": token}
        )

        email_subject = "Password Reset Requested"
        email_body = f"Follow this link to set a new password:\n\n{reset_url}"

        send_mail(
            email_subject,
            email_body,
            EMAIL_HOST,
            [email],
        )
        return Response(
            {"success": "A password reset email has been sent"},
            status=status.HTTP_200_OK,
        )
    return Response(
        {"error": "An email address is required"},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["POST"])
def password_reset_confirm(request: Request, uidb64, token):
    decoded_uidb64 = urlsafe_base64_decode(uidb64).decode()

    try:
        user = User.objects.get(pk=decoded_uidb64)
    except User.DoesNotExist:
        return Response(
            {"error": "User does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if default_token_generator.check_token(user, token):
        password = request.data.get("password")

        if password:
            user.set_password(password)
            user.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return Response(
                {"success": "Your password has been reset"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "A password is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response({"error": "The reset password link is no longer valid"})
