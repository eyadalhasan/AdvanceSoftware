# customuserapp/urls.py
from django.urls import path, include
from .views import RegistrationView, LoginView, SignOutView, UpdateProfileView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"", UpdateProfileView, basename="")


urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", SignOutView.as_view(), name="logout"),
    path("", include(router.urls)),
]
