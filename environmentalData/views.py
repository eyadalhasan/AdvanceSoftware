from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets

from .models import EnviromentalData
from .serializer import EnvironmentalDataSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import EnviromentalData


class EnvironmentalDataViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = EnviromentalData.objects.all()
    serializer_class = EnvironmentalDataSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_air_quality(self, request, pk=None):
        air_quality = request.query_params.get("air_quality", None)
        if air_quality is None:
            return Response(
                {"error": "air_quality parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = EnviromentalData.objects.filter(air_quality=int(air_quality))
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_temperature(self, request, pk=None):
        temperature = request.query_params.get("temperature", None)
        if temperature is  None:
            return Response(
                {"error": "temperature parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = EnviromentalData.objects.filter(temperature=int(temperature))
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_humidity(self, request, pk=None):
        humidity = request.query_params.get("humidity", None)
        if humidity is  None:
            return Response(
                {"error": "humidity parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = EnviromentalData.objects.filter(humidity=int(humidity))
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_water_quality(self, request, pk=None):
        water_quality = request.query_params.get("water_quality", None)
        if water_quality is  None:
            return Response(
                {"error": "water_quality parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = EnviromentalData.objects.filter(water_quality=int(water_quality))
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_biodiversity_metrics(self, request, pk=None):
        biodiversity_metrics = request.query_params.get("biodiversity_metrics", None)
        if biodiversity_metrics is None:
            return Response(
                {"error": "biodiversity_metrics parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = EnviromentalData.objects.filter(
            biodiversity_metrics=int(biodiversity_metrics)
        )
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_city(self, request, pk=None):
        city = request.query_params.get("city", None)
        if city is  None:
            return Response(
                {"error": "city parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = EnviromentalData.objects.filter(city__iexact=city)
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)
