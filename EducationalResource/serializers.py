# customuserapp/serializers.py
from rest_framework import serializers
from EducationalResource.models import EducationalResource


class EducationalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalResource
        fields = '__all__'
