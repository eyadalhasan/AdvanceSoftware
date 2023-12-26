from django.shortcuts import render
from rest_framework import viewsets
from EducationalResource.models import EducationalResource
from EducationalResource.serializers import EducationalResourceSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import EducationalResource


class EducationalResourceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = EducationalResource.objects.all()
    serializer_class = EducationalResourceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_title(self, request, pk=None):
        title = request.query_params.get("title", None)
        if not title:
            return Response(
                {"error": "title parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = EducationalResource.objects.filter(title__iexact=title)
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
        objs = EducationalResource.objects.filter(report_type__iexact=type)
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_content(self, request, pk=None):
        content = request.query_params.get("content", None)
        if not content:
            return Response(
                {"error": "content parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = EducationalResource.objects.filter(content__icontains=content)
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_by_author(self, request, pk=None):
        author = request.query_params.get("author", None)
        if not author:
            return Response(
                {"error": "author parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        objs = EducationalResource.objects.filter(author__iexact=author)
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)
