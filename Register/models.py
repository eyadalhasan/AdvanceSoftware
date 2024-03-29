from django.db import models

# Create your models here.
# customuserapp/models.py
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(
        self, username, email, password=None, role="", phone_number="", **extra_fields
    ):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            role=role,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, email, password=None, role="", phone_number="", **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(
            username, email, password, role, phone_number, **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    city = models.CharField(max_length=255, blank=True, null=True, default="")
    interests = models.CharField(max_length=255, default="", blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    objects = CustomUserManager()
    threshold_humidity = models.FloatField(null=True, blank=True, default=0)
    threshold_temperature = models.FloatField(null=True, blank=True, default=0)
    threshold_water_quality = models.FloatField(null=True, blank=True, default=0)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
