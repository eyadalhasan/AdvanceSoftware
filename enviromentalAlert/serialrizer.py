from rest_framework import serializers
from .models import EnvironmentalAlert


class EnvironmentalAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalAlert
        fields = "__all__"
