from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets

from .models import EnviromentalData
from .serializer import EnvironmentalDataSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
class EnvironmentalDataViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = EnviromentalData.objects.all()
    serializer_class = EnvironmentalDataSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
