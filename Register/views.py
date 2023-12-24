from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


class RegistrationView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, format=None):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data["password"])
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# customuserapp/views.py


class LoginView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        print(username)
        print(password)
        print(email)
        user = authenticate(request, username=username, password=password, email=email)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"token": str(token)}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "Account is not active"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"message": "Invalid login credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class SignOutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get the user's token
        user_token = request.auth
 
        if user_token:
            # Delete the user's token
            user_token.delete()
            # logout(request.user)

            return Response(
                {"detail": "Successfully logged out."}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "No authentication token provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )
