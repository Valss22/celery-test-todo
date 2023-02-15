from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


@api_view(["POST"])
def user_login(self, request: Request):
    username = request.data["username"]
    password = request.data["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # do some authorization based on user roles or permissions
        return Response(
            {"message": "Authentication successful."}, status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED
        )
