from rest_framework import serializers
from .models import Score


class serializerScore(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = "__all__"