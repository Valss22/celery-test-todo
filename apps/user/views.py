from django.contrib.auth import authenticate, login
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
            {"message": "Authentication successful."}, status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED
        )
