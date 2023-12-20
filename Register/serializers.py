# customuserapp/serializers.py
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "_all_"
        extra_kwargs = {"password": {"write_only": True}}
