from django.shortcuts import render
from .models import EnvironmentalAlert
from rest_framework import viewsets
from .serialrizer import EnvironmentalAlertSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import EnvironmentalAlert


class EnvironmentalAlertViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = EnvironmentalAlert.objects.all()
    serializer_class = EnvironmentalAlertSerializer
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_message(self, request, pk=None):
        message = request.query_params.get("message", None)
        if not message:
            return Response(
                {"error": "message parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = EnvironmentalAlert.objects.filter(message__icontains=message)
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)
