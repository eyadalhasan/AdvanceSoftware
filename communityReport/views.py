from django.shortcuts import render
from rest_framework import viewsets
from .models import CommunityReport
from .serializer import CommunityReportSerializer


class CommunityReportViewSet(viewsets.ModelViewSet):
    queryset = CommunityReport.objects.all()
    serializer_class = CommunityReportSerializer
