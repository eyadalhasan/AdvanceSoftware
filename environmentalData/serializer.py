from rest_framework import serializers
from .models import EnviromentalData


class EnvironmentalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnviromentalData
        fields = "__all__"
        
