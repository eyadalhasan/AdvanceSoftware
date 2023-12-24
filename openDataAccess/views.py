from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from environmentalData.models import EnviromentalData
from django.db.models import Avg, Count
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class OpenDataAccessView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        ROLE_CHOICES = ["scientist", "researcher", "organization"]
        data = request.data

        print(str(request.user.role) in ROLE_CHOICES)

        if request.user.role not in ROLE_CHOICES:
            return Response(
                {
                    "error": "Permission denied. User must have scientist or researh or organization role."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        aggregated_data = EnviromentalData.objects.aggregate(
            avg_air_quality=Avg("air_quality"),
            avg_temperature=Avg("temperature"),
            avg_humidity=Avg("humidity"),
            total_records=Count("id"),
        )

        return Response(aggregated_data)
