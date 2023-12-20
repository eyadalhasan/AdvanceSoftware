from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets

from .models import EnviromentalData
from .serializer import EnvironmentalDataSerializer


class EnvironmentalDataViewSet(viewsets.ModelViewSet):
    queryset = EnviromentalData.objects.all()
    serializer_class = EnvironmentalDataSerializer
