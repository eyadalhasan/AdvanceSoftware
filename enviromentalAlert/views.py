from django.shortcuts import render
from .models import EnvironmentalAlert
from rest_framework import viewsets
from .serialrizer import EnvironmentalAlertSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
class EnvironmentalAlertViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = EnvironmentalAlert.objects.all()
    serializer_class = EnvironmentalAlertSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
