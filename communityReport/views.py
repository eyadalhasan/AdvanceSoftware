from django.shortcuts import render
from rest_framework import viewsets
from .models import CommunityReport
from .serializer import CommunityReportSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CommunityReportViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = CommunityReport.objects.all()
    serializer_class = CommunityReportSerializer


from rest_framework import viewsets


class CommunityReportViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = CommunityReport.objects.all()
    serializer_class = CommunityReportSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
