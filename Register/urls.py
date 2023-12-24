# customuserapp/urls.py
from django.urls import path
from .views import RegistrationView, LoginView, SignOutView

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", SignOutView.as_view(), name="logout"),
]
