from .models import CommunityReport
from rest_framework import serializers


class CommunityReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityReport
        fields = "__all__"
        # depth=1