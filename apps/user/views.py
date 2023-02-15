from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


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
def user_password_change(request: Request):
    form = PasswordChangeForm(user=request.user, data=request.data)

    if form.is_valid():
        form.save()
        return Response(
            {"message": "Password changed successfully"},
            status=status.HTTP_200_OK,
        )

    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
