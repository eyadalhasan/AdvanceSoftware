from django.shortcuts import render
from .models import EnvironmentalAlert
from rest_framework import viewsets
from .serialrizer import EnvironmentalAlertSerializer


class EnvironmentalAlertViewSet(viewsets.ModelViewSet):
    queryset = EnvironmentalAlert.objects.all()
    serializer_class = EnvironmentalAlertSerializer
    