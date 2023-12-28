from django.shortcuts import render
from rest_framework import viewsets
from .models import CommunityReport
from .serializer import CommunityReportSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
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

    @action(detail=False, methods=["get"])
    def get_by_city(self, request, pk=None):
        city = request.query_params.get("city", None)
        if not city:
            return Response(
                {"error": "City parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = CommunityReport.objects.filter(city__iexact=city)
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_type(self, request, pk=None):
        type = request.query_params.get("type", None)
        if not type:
            return Response(
                {"error": "type parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = CommunityReport.objects.filter(report_type__iexact=type)
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_description(self, request, pk=None):
        description = request.query_params.get("description", None)
        if not description:
            return Response(
                {"error": "description parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = CommunityReport.objects.filter(description__icontains=description)
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    # @action(detail=False,methods=['get'])
    # def get_by_user(self,request,pk=None):
    #     user=
    # objs = CommunityReport.objects.filter(description__icontains=description)
    # serializer = self.get_serializer(objs, many=True)
    # return Response(serializer.data)
